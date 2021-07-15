a, b = map(int, input().split())

ans = 0
for _ in range(2):
    choice = max(a, b)
    ans += choice
    if choice == a:
        a -= 1
    else:
        b -= 1

print(ans)
