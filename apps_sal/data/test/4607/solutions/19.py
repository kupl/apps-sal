a, b = map(int, input().split())

ans = a - 1

if b >= a:
    print(ans + 1)
else:
    print(ans)
