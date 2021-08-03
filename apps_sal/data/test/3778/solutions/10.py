from sys import stdin
import sys

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

one = []
ttt = []
ans = []

for i in range(n, 0, -1):

    now = a[i - 1]
    if now == 0:
        continue
    elif now == 1:
        ans.append((i, i))
        one.append(i)
    elif now == 2:
        if len(one) == 0:
            print(-1)
            return
        ans.append((one[-1], i))
        del one[-1]
        ttt.append(i)
    elif now == 3:
        if len(ttt) == 0:
            if len(one) == 0:
                print(-1)
                return
            ans.append((i, i))
            ans.append((i, one[-1]))
            del one[-1]
            ttt.append(i)
        else:
            ans.append((i, i))
            ans.append((i, ttt[-1]))
            del ttt[-1]
            ttt.append(i)

print(len(ans))
for i in ans:
    print(*i)
