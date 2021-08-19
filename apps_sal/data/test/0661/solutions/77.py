from collections import deque
(m, k) = map(int, input().split())
if k >= pow(2, m):
    print(-1)
elif m == 0:
    print(0, 0)
elif m == 1:
    if k == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    ans = deque()
    ans.append(k)
    for i in range(pow(2, m)):
        if i != k:
            ans.append(i)
            ans.appendleft(i)
    ans.append(k)
    print(' '.join(map(str, ans)))
