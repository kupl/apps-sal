N = int(input())
H = list(map(int, input().split()))
i = 0
ans = 0
t = 0
while i < N - 1:
    if H[i] < H[i + 1]:
        ans = max(ans, t)
        t = 0
    else:
        t += 1
    i += 1
ans = max(ans, t)
print(ans)
