from collections import deque
S = deque(list(input()))
q = int(input())
flag = False
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1' and flag == False:
        flag = True
    elif query[0] == '1' and flag == True:
        flag = False
    elif flag == False and query[1] == '1' or (flag == True and query[1] == '2'):
        S.appendleft(query[2])
    else:
        S.append(query[2])
if flag:
    S = list(S)[::-1]
else:
    S = list(S)
print(''.join(map(str, list(S))))
