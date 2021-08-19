'''
----BRUTE (but is also smart)----
KEY: use a set to hold all elements of input array.
So if you find a+b in the set, you can keep moving forward and updating 1 \"jump\" forward for a-->b, b--> a+b.
Then continue. So change the if-check to a while loop.

get every pair (i,j)
    then try to find their next value in set. If found then update 
        holdj = j
        j = i+j
        i = holdj
        len++
    res = max(res,len)
return res if res>2
----big-O----
O((N^2) * logM)
N^2 to get each pair.
logM to get to the end of each fibonacci \"chain\"

----dp----
dp[a,b] = len of fib sequence ending with a,b
dp[a,b] = dp[b-a,a]+1 , if val[b]-val[a] <val[a] and (val[b]-val[a]) exists in set
        = 2            , if (val[b]-val[a],val[a]) doesnt exist in dp
return the max of all dp cells, or [0]
---big-O--
O(N^2) for nested loop.

        
'''


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        res = 0
        if len(A) <= 2:
            return 0
        find = set(A)
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                currLen = 2
                a = A[i]
                b = A[j]
                while (a + b) in find:
                    currLen += 1
                    holdb = b  # you're not moving along i and j, but the actual values themselves. Because you already have the values you need in the set.
                    b = a + b
                    a = holdb
                    res = max(currLen, res)
        if res > 2:
            return res
        else:
            return 0
