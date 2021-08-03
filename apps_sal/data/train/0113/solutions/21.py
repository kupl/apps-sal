T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    d = abs(a - b)

    ans = (d // 5)

    d = d % 5

    if d == 1 or d == 2:
        ans += 1

    if d == 3 or d == 4:
        ans += 2

    print(ans)
