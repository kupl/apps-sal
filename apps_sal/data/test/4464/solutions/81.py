(a, b, c) = map(int, input().split())
ans = 'NO'
for i in range(1, b + 1):
    mod = a * i % b
    if mod == 0:
        continue
    elif c % mod == 0:
        ans = 'YES'
        break
print(ans)
