getint = lambda: int(input())
getints = lambda: map(int, input().split())
getlist = lambda: list(getints())
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
