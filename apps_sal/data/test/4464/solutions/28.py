
a, b, c = map(int, input().split())
ans = 'NO'

for i in range(b):
    num = i * a
    mod = num % b
    if mod == c:
        ans = 'YES'
        break
print(ans)
