import sys
import copy
import os

# sys.stdin = open(os.path.join(os.path.dirname(__file__), '2.in'))


def solve():
    MOD = int(1e9+7)

    f = 0
    n = int(input())

    s = input()

    alphabet ={ chr(ord('a')+i):num for i,num in enumerate( map(lambda x :int(x),input().split()) ) }
    dp =[0 for _ in range(n)]; minlen = 2<<20; maxlen=0
    minsplitnum =[2<<20 for _ in range(n)]

    def check(newstr,start,end):
        nl = end-start
        while start < end:
            if alphabet[newstr[start]] < nl:
                return False 
            start+=1
        # print(newstr)
        return True

    i = 0
    while i < n:
    # for i in range(n):
        if i == 0:
            dp[i] = 1
            maxlen = 1
            minsplitnum[i] = 1
        else:
            f = 0
            # divide the element to one
            dp[i] = (dp[i-1] + dp[i])%MOD 
            minsplitnum[i] = minsplitnum[i-1]+1 if minsplitnum[i] > minsplitnum[i-1]+1 else minsplitnum[i]
            # divide the element to before
            j = i-1
            f = i + 1 - alphabet[s[i]] if i + 1 - alphabet[s[i]] > f else f
            while j >= 0:
                # print('j',j)
                f = i + 1 - alphabet[s[j]] if i + 1 - alphabet[s[j]] > f else f
                if j >= f:
                    if j == 0:
                        dp[i] = (1 + dp[i])%MOD 
                    else:
                        dp[i] = (dp[j-1] + dp[i])%MOD 
                    maxlen = i-j+1 if i -j + 1 > maxlen else maxlen
                    if j == 0:
                        minsplitnum[i] = 1 if 1 < minsplitnum[i] else minsplitnum[i]
                    else:
                        minsplitnum[i] = minsplitnum[j-1]+1 if minsplitnum[j-1]+1 < minsplitnum[i] else minsplitnum[i]
                    j -= 1
                else:
                    j -= 1
                    continue
                
        i += 1
        # print(dp[i])
    print(int(dp[n-1]))
    print(maxlen)
    print(int(minsplitnum[n-1]))


solve()
