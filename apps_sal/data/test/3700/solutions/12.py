n, m = list(map(int, input().split()))
b = m // 2
if m % 2 == 0:
    a = b
else:
    a = b + 1
if a == b:
    a += 1
    b -= 1

ans = min(n, m - 1) - a + 1
if ans <= 0:
    print(0)
else:
    print(ans)
