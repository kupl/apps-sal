import itertools
N = int(input())
F =[ list(input().split()) for i in range(N)]
P =[ list(input().split()) for i in range(N)]
set01 = list(itertools.product('01',repeat = 10))
counter = []
ans = -10**9
for s01 in set01:
    if s01 != ("0","0","0","0","0","0","0","0","0","0"):
        prof = 0
        for i in range(N):
            counter = 0
            for j in range(10):
                if s01[j] =="1" and F[i][j] == "1":
                    counter += 1
            prof += int(P[i][counter])
        ans = max(ans,prof)
print(ans)
