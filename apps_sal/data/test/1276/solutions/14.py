n = int(input())
s = list(input())
count = s.count('R') * s.count('G') * s.count('B')
for i in range(n - 2):
    for j in range(1, (n + 1 - i) // 2):
        if sorted([s[i], s[i + j], s[i + 2 * j]]) == ['B', 'G', 'R']:
            count -= 1
print(count)
