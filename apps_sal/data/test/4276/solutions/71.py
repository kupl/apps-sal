N, T = map(int, input().split())
k = 1001
for i in range(N):
    c, t = map(int, input().split())
    if t <= T and c < k:
        k = c
if k == 1001:
    print("TLE")
    return
print(k)
