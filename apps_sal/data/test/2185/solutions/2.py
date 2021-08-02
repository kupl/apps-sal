from sys import stdin
from collections import deque
t = int(stdin.readline().strip())

for cas in range(t):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    s1 = list(map(int, stdin.readline().strip().split()))
    aux = deque([])
    for i in range(n):
        aux.append(s[i] - s1[i])
    l = n
    r = -1
    for i in range(n):
        if aux[i] != 0:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if aux[i] != 0:
            r = i
            break
    st = set()
    for i in range(l, r + 1):
        st.add(aux[i])
    st = list(st)
    if len(st) == 0 or (len(st) == 1 and st[0] < 0):
        print("YES")
    else:
        print("NO")
