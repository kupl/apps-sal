def getint(): return int(input())
def getints(): return map(int, input().split())
def getlist(): return list(getints())


n = getint()
a = getlist()
a.sort(reverse=True)
alice = bob = 0
for i in range(n):
    if i % 2:
        bob += a[i]
    else:
        alice += a[i]
print(alice - bob)
