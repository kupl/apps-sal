n = int(input())
arr = []
for i in range(n):
    s = input()
    arr.append((len(s), s))
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
"\nn, k = map(int, input().split())\narr = list(map(int, input().split()))\nfor i in range(n):\n    arr[i] = (arr[i], i + 1)\narr.sort()\n\ncur = -1\nans = []\nfor i in range(n):\n    if arr[i][0] != cur:\n        ans.append(arr[i][1])\n        cur = arr[i][0]\n    if len(ans) == k:\n        break\nif len(ans) == k:\n    print('YES')\n    print(*ans)\nelse:\n    print('NO')\n    "
