(n, m) = map(int, input().split())
for i in range(n):
    row = input()
    if 'B' in row:
        left = row.find('B')
        right = row.rfind('B')
        a = right - left + 1
        print(i + a // 2 + 1, left + a // 2 + 1)
        break
