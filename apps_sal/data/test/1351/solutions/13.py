(l, r) = map(int, input().split())


def alldiff(i):
    s = list(str(i))
    m = set(s)
    if len(s) == len(m):
        return True
    return False


for i in range(l, r + 1):
    if alldiff(i):
        print(i)
        quit()
print(-1)
