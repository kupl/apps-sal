from collections import deque
n = int(input())
#a, b, c = map(int, input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

q = deque([])

for i in range(1, n + 1):
    if i % 2 == 0:
        q.appendleft(al[i - 1])
    else:
        q.append(al[i - 1])

ansl = list(q)
ansl = ansl[::-1] if n % 2 != 0 else ansl

print(*ansl, sep=" ")
