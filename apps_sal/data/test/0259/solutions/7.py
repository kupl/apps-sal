N, T = list(map(int, input().split()))
mi = 10**100
for i in range(N):
    s, d = list(map(int, input().split()))
    if s >= T:
        a = s - T
    else:
        a = (s - T) % d
    if a < mi:
        mi = a
        ans = i + 1
print(ans)

