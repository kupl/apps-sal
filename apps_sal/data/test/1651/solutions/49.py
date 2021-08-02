S, P = map(lambda x: int(x), input().split())
ans = "No"

for n in range(1, int(P**(1 / 2)) + 1):
    if n + P / n == S:
        ans = "Yes"

print(ans)
