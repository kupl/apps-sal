import bisect
N = int(input())
lsA = list(map(int,input().split()))
lsB = list(map(int,input().split()))
lsC = list(map(int,input().split()))
lsA.sort()
lsB.sort()
lsC.sort()
ans = 0
for i in range(N):
    B = lsB[i]
    indexA = bisect.bisect(lsA,B-1)
    indexC = N - bisect.bisect(lsC,B)
    ans += indexA*indexC
print(ans)
