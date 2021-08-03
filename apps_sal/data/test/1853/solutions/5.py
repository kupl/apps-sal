n, m = list(map(int, input().split()))
member = [0 for _ in range(n + 1)]
linked = set()
for i in range(m):
    a, b = list(map(int, input().split()))
    linked.add(str(a) + '-' + str(b))
    linked.add(str(b) + '-' + str(a))
    member[a] += 1
    member[b] += 1
num = 0
for i in range(1, n + 1):
    if member[i] < n - 1:
        num = i
        break
# print(linked)
if num:
    for i in range(1, n + 1):
        if i != num:
            text = str(num) + '-' + str(i)
            if text not in linked:
                pair = i
                break
    arr = [num, pair]
    arr.sort()
    sa = [0] * n
    sb = [0] * n
    sa[arr[0] - 1] = 1
    sa[arr[1] - 1] = 2
    sb[arr[0] - 1] = 1
    sb[arr[1] - 1] = 1
    cur = 3
    for i in range(n):
        if sa[i] == 0:
            sa[i] = cur
            sb[i] = cur
            cur += 1
    print('YES')
    print(*sa)
    print(*sb)
else:
    print('NO')
