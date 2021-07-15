n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append((len(s),s))
arr.sort()
fl = True
for i in range(n - 1):
    if arr[i + 1][1].find(arr[i][1]) == -1:
        fl = False
        break
if fl:
    print('YES')
    for i in arr:
        print(i[1])
else:
    print('NO')
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (arr[i], i + 1)
arr.sort()

cur = -1
ans = []
for i in range(n):
    if arr[i][0] != cur:
        ans.append(arr[i][1])
        cur = arr[i][0]
    if len(ans) == k:
        break
if len(ans) == k:
    print('YES')
    print(*ans)
else:
    print('NO')
    '''
