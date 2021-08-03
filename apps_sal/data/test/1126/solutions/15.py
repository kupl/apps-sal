import sys

sys.setrecursionlimit(10**6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


n, x, md = MI()
# n,x,md=6,7,13
pos = [-1] * md
aa = []
if x == 0:
    print(0)
    return

for i in range(md):
    if pos[x] != -1:
        p = pos[x]
        c = i - pos[x]
        # print(x,i,pos[x])
        break
    aa.append(x)
    pos[x] = i
    x = pow(x, 2, md)
cs = sum(aa[p:])

# print(p,c)
# print(pos)
# print(aa)

if n <= len(aa):
    print(sum(aa[:n]))
    return

n -= p
cnt = n // c
n %= c
n += p
print(cs * cnt + sum(aa[:n]))
