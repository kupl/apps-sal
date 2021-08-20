(n, m) = list(map(int, input().split()))
arr = []
for i in range(n):
    bulbs = list(map(int, input().split()))
    bulbs = bulbs[1:]
    arr.extend(bulbs)
if len(set(arr)) == m:
    print('YES')
else:
    print('NO')
