from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    bckt = []
    for i in range(n):
        if not l[i]:
            bckt.append(a[i])
            a[i] = 10**9

    bckt.sort(reverse=True)
    bckt = deque(bckt)

    for i in range(n):
        if a[i] == 10**9:
            a[i] = bckt.popleft()

    print(*a)
