(a, b, c) = map(int, input().split())
res = 'NO'
for i in range(b):
    if a * i % b == c:
        res = 'YES'
        break
print(res)
