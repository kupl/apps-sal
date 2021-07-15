from collections import Counter

N = int(input())
S = input()
cnt = Counter(S)

ans = cnt['R']*cnt['G']*cnt['B']
#まずansに要請１を満たす(i, j, k)の組の数を入れておき，ここから，要請２を満たさないものを除いていく。

for i in range(N-2):
    for j in range(i+1, N-1):
        k = j + (j - i)
        #kは　j - i = k - j を満たす。ただし，（i, j, k）が要請１を満たしているとは限らない。
        if k < N:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1

print(ans)
