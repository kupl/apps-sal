a = int(input())
lister = input().split()
lister = [int(i) for i in lister]
ans = dict()


def findans(n):
    if n in ans:
        return ans[n]
    mod = n % lister[n]
    ok = True
    if n + lister[n] >= a and n - lister[n] < 0:
        ok = False
    else:
        for i in range(mod, a, lister[n]):
            if i != n and lister[i] > lister[n]:
                ok = ok and findans(i)
        ok = not ok
    ans[n] = ok
    return ok


for i in range(len(lister)):
    findans(i)
level = []
for i in range(a):
    if ans[i] == True:
        level.append('A')
    else:
        level.append('B')
print(''.join(level))
