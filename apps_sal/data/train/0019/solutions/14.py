from collections import deque
t = int(input())
for jfrhg in range(t):
    (n, k, d) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l = deque(a[:d])
    s = dict()
    for i in l:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
    minimum = len(list(s.keys()))
    for i in range(d, n):
        ref = l.popleft()
        l.append(a[i])
        s[ref] -= 1
        if s[ref] < 1:
            del s[ref]
        if a[i] in s:
            s[a[i]] += 1
        else:
            s[a[i]] = 1
        if len(list(s.keys())) < minimum:
            minimum = len(list(s.keys()))
    print(minimum)
