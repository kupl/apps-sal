def right(m, n, a):
    b = True
    n2 = a // 2 - a // 6
    n3 = a // 3 - a // 6
    n6 = a // 6
    if n2 + n6 < n or n3 + n6 < m or n2 + n3 + n6 < n + m:
        b = False
    return b


n, m = list(map(int, input().split()))
ans = n + m
while not right(m, n, ans):
    ans += 1
print(ans)
