import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    dic = {}
    for i, a in enumerate(A):
        if not a in dic:
            dic[a] = [i]
        else:
            dic[a].append(i)
    
    ok = False
    for L in dic.values():
        if len(L) > 1 and L[-1] - L[0] > 1:
            ok = True
            break
    print("YES" if ok else "NO")
