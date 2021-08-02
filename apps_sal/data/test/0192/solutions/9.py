x, y = list(map(int, input().split()))
x, y = min(x, y), max(x, y)
a, b, c = x, x, x
ans = 0
while (not a == b == c == y):
    a = min(b + c - 1, y)
    ans += 1
    if (not a == b == c == y):
        b = min(a + c - 1, y)
        ans += 1
        if (not a == b == c == y):
            c = min(a + b - 1, y)
            ans += 1
        else:
            break
    else:
        break

print(ans)
