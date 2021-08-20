n = int(input())
ans = 0
for _ in range(n):
    (v, t) = input().split()
    if t == 'JPY':
        ans += int(v)
    else:
        ans += float(v) * 380000
print(ans)
