n = int(input())
def r():
    return [int(i) for i in input().split()]

deg = r(), r(), r()

l = [i[0] for i in deg]
def remains():
    return n - sum(l)

def better(i):
    nonlocal l
    rem = remains()
    l[i] = min(l[i]+rem, deg[i][1])

for i in range(len(l)):
    better(i)

print(" ".join(str(i) for i in l))

