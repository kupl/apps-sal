a, b, c = map(int, input().split())
n = a
ans = 'NO'
for i in range(1, b + 1):
    if n % b == c:
        ans = 'YES'
        break
    else:
        n += a
print(ans)
