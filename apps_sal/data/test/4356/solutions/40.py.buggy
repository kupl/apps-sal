n, m = map(int, input().split())

alist = [input() for _ in range(n)]
blist = [input() for _ in range(m)]


def match(i, j):
    for di in range(m):
        for dj in range(m):
            if alist[i + di][j + dj] != blist[di][dj]:
                return False
    return True


for i in range(n - m + 1):
    for j in range(n - m + 1):
        if match(i, j):
            print("Yes")
            return

print("No")
