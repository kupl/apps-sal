import sys

def isDoomed(l):
    s = set(l)
    for e in s:
        if -e in s:
            return False
    return True

n, m = map(int, input().split())
for mm in range(m):
    l = list(map(int, input().split()))[1:]
    if isDoomed(l):
        print('YES')
        return
print('NO')
