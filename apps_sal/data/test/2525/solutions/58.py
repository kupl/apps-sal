from collections import deque
d = deque()
S = input()
d.append(S)
Q = int(input())
query = [list(input().split()) for _ in range(Q)]
rev = 0
for i in range(Q):
    if query[i][0] == str(1):
        rev += 1
    elif rev % 2 == 0:
        if query[i][1] == str(1):
            d.appendleft(query[i][2])
        else:
            d.append(query[i][2])
    elif query[i][1] == str(1):
        d.append(query[i][2])
    else:
        d.appendleft(query[i][2])
ans = ''.join(list(d))
if rev % 2 != 0:
    ans = ans[::-1]
print(ans)
