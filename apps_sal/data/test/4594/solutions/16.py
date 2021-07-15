import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
D = []
for i in range(N):
    d = int(input())
    D.append(d)

D_set = set(D)
ans = len(D_set)

print(ans)
