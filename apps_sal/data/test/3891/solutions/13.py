(n, m) = map(int, input().split())
for i in range(n):
    s = input()
    if 'B' in s:
        l = s.count('B')
        print(i + l // 2 + 1, s.index('B') + l // 2 + 1)
        break
