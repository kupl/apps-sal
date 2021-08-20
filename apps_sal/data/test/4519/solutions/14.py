from collections import deque
for __ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ar = list(map(int, input()))
    lol = deque([])
    for i in range(n):
        if ar[i] == 0:
            lol.append(i)
    i = 0
    while lol and len(lol) > i and (lol[i] == i):
        i += 1
    num = i
    for __ in range(i):
        lol.popleft()
    while lol and k > 0:
        x = lol[0]
        if k >= x - num:
            k -= x
            k += num
            lol.popleft()
            i += 1
            num += 1
        else:
            break
    ans = []
    for j in range(i):
        ans.append(0)
    if lol:
        lol[0] -= k
    for j in range(i, n):
        if lol and j == lol[0]:
            ans.append(0)
            lol.popleft()
        else:
            ans.append(1)
    print(''.join(map(str, ans)))
