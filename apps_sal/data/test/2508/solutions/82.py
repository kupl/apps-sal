from collections import deque
def ii(): return int(input())
def iim(): return list(map(int, input().split()))
def iil(): return list(map(int, input().split()))


def bfs(xg, yg):
    queue = deque([(xs, ys, 0)])
    while queue:
        x, y, dep = queue.popleft()
        l = []
        f1 = True
        f2 = True
        f3 = True
        f4 = True
        for i in range(1, k + 1):
            if f1:
                if cord[y][x + i] == '.':
                    l.append((x + i, y))
                elif cord[y][x + i] == '@' or cord[y][x + i] != dep + 1:
                    f1 = False
            if f2:
                if cord[y][x - i] == '.':
                    l.append((x - i, y))
                elif cord[y][x - i] == '@' or cord[y][x - i] != dep + 1:
                    f2 = False
            if f3:
                if cord[y + i][x] == '.':
                    l.append((x, y + i))
                elif cord[y + i][x] == '@' or cord[y + i][x] != dep + 1:
                    f3 = False
            if f4:
                if cord[y - i][x] == '.':
                    l.append((x, y - i))
                elif cord[y - i][x] == '@' or cord[y - i][x] != dep + 1:
                    f4 = False
            if not (f1 or f2 or f3 or f4):
                break
        for nx, ny in l:
            if cord[ny][nx] == '.':
                cord[ny][nx] = dep + 1
                if (nx, ny) == (xg, yg):
                    return dep + 1
                else:
                    queue.append((nx, ny, dep + 1))
    return -1


h, w, k = iim()
ys, xs, yg, xg = iim()

cord = [['@'] * (w + 2)]
for i in range(h):
    cord.append(['@'] + list(input()) + ['@'])
cord.append(['@'] * (w + 2))
cord[ys][xs] = '#'
# for i in cord:
#    print(*i)
# print(len(cord),len(cord[0]))

print((bfs(xg, yg)))
