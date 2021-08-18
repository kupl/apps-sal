
N = int(input())

ans = 0

for i in range(1, N + 1):
    S = list(str(i))
    if len(S) % 2 == 1:
        ans += 1
print(ans)
