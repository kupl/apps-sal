from collections import deque
t = int(input())
for i in range(t):
    n = list(map(int, input()))
    chet, nechet = deque(), deque()
    for el in n:
        if el % 2 == 0:
            chet.append(el)
        else:
            nechet.append(el)
    ans = []
    while chet or nechet:
        if chet and nechet:
            if chet[0] < nechet[0]:
                ans.append(chet.popleft())
            else:
                ans.append(nechet.popleft())
        elif chet:
            ans.append(chet.popleft())
        else:
            ans.append(nechet.popleft())
    print(''.join(map(str, ans)))
