(a, b, c) = map(int, input().split())
s = 'NO'
for i in [a * j for j in range(1, b)]:
    if i % b == c:
        s = 'YES'
        break
print(s)
