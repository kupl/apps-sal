from collections import deque
for _ in range(int(input())):
    x = input()
    even = deque()
    odd = deque()
    for i in map(int, x):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    ans = deque()
    while len(ans) < len(x):
        if len(even) == 0:
            ans.append(odd.popleft())
        elif len(odd) == 0:
            ans.append(even.popleft())
        elif even[0] < odd[0]:
            ans.append(even.popleft())
        else:
            ans.append(odd.popleft())
    print(''.join((str(i) for i in ans)))
