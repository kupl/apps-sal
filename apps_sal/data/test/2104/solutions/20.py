(l, r) = list(map(int, input().split(' ')))
print('YES')
r += 1
pairs = (r - l) // 2
for i in range(pairs):
    print(l + 2 * i, l + 2 * i + 1)
