import sys
import queue
n, = map(int, input().split())

rs, cs = map(int, input().split())
rd, cd = map(int, input().split())
rs -= 1
cs -= 1
rd -= 1
cd -= 1


E = []
for i in range(0, n):
    E.append(list(input().split('\n')[0]))

S = []
D = []

q = queue.Queue()
q.put((rs, cs))


def get_all_dirs(e):
    dirs = []
    a, b = e[0], e[1]
    if a + 1 < n:
        dirs.append((a + 1, b))
    if a - 1 >= 0:
        dirs.append((a - 1, b))
    if b + 1 < n:
        dirs.append((a, b + 1))
    if b - 1 >= 0:
        dirs.append((a, b - 1))
    return dirs


def process_dirs(e):
    dirs = get_all_dirs(e)
    water = False
    for d in dirs:
        if E[d[0]][d[1]] == '1':
            water = True
        elif E[d[0]][d[1]] == '0':
            q.put(d)
            E[d[0]][d[1]] = '2'
    return water


while not q.empty():
    e = q.get()
    water = process_dirs(e)
    if e[0] == rd and e[1] == cd:
        print(0)
        return
    if water:
        S.append(e)


q.put((rd, cd))

while not q.empty():
    e = q.get()
    water = process_dirs(e)
    if water:
        D.append(e)


def square(a):
    return a * a


def dis(a, b):
    return square(a[0] - b[0]) + square(a[1] - b[1])


ans = sys.maxsize
for i in S:
    for j in D:
        ans = min(ans, dis(i, j))

print(ans)
