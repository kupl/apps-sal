"""
[9,4,7,2,10]
 i
          j

:  (freq, diff)
{9: {0:1}, 
{4: {0,1}, {-5, 2}}
{7: {0,1}, {-2,2}, {3,2}}
{2: {0,1}, {-7:2}, {-2, 2}, {-5,2}}
{10:{0,1}, {1, 2}, {6,2}, {3,3}}
 
 [20,1,15,3,10,5,8]
  i       j
  
  {
  20:(1,0)
  1:(2,-19)
  15:(2,-5)
  3(4,5)
  
}

So we keep running hashmap of all numbers we meet along with its available arith difference along with its frequency. Then we do n^2 loop through all numbers, each time calculating the difference between number i and number j and trying to see if there is that difference avaible in the hashmap of j pointer. At this point if there is a difference match, we add on, else we start at frequency of.

then we can keep track of max throughout and return the max

O(n^2)
O(n^2)


"""


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        d = collections.defaultdict(dict)
        sol = 0
        for i in range(1, len(A)):
            for j in range(i):
                curDiff = A[i] - A[j]
                if curDiff in d[j]:
                    d[i][curDiff] = d[j][curDiff] + 1
                else:
                    d[i][curDiff] = 2
                sol = max(sol, d[i][curDiff])
        return sol
