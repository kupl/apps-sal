# ABC112

N, T = list(map(int, input().split()))
C_T = [list(map(int, input().split())) for _ in range(N)]
temp_c = 10**10
for c, t in C_T:
    if t <= T and c <= temp_c:
        temp_c = c


if temp_c == 10**10:
    ans = "TLE"
else:
    ans = temp_c
print(ans)
