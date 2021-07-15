import collections

N = int(input())
A = list(map(int,input().split()))
Ac = collections.Counter(A)
ans = sum(A)

Q = int(input())

for _ in range(Q):
    B,C = map(int,input().split())
    numB = Ac[B]
    ans += (C-B)*numB
    print(ans)
    Ac[C]+=numB
    Ac[B]=0
