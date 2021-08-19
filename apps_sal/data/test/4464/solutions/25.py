(a, b, c) = list(map(int, input().split()))
ans = []
for i in range(1, b + 1):
    ans.append(a * i % b)
print('YES' if c in ans else 'NO')
