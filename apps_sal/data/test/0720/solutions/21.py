n = int(input())
a_0 = b_0 = 0
r = 1
for _ in range(n):
    a, b = list(map(int, input().split()))

    if a_0 > b_0:
        if a > b:
            r += max(0, b - a_0 + 1)
        else:
            r += a - a_0 + 1
    elif a_0 < b_0:
        if b > a:
            r += max(0, a - b_0 + 1)
        else:
            r += b - b_0 + 1
    else:
        r += min(a, b) - a_0
    a_0, b_0 = a, b
print(r)

