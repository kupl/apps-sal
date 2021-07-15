import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
S = list(input())

def judge(ai, bi):
    a, b = S[ai%N], S[bi%N]
    if a==b:
        return ai
    elif (a=='R' and b=='S') or (a=='P' and b=='R') or (a=='S' and b=='P'):
        return ai
    else:
        return bi

def fight(lis):
    length = len(lis)
    ret = []
    for i in range(0, length, 2):
        ret.append(judge(lis[i], lis[i+1]))
    return ret

old = list(range(N))
for _ in range(K):
    old = fight(old*2)
print(S[old[0]])
