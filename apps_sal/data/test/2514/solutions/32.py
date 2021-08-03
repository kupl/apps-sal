import collections

N = int(input())
A = list(map(int, input().split()))
Ac = collections.defaultdict(int)
ans = 0
for a in A:
    Ac[a] += 1
    ans += a

Q = int(input())

for _ in range(Q):
    B, C = map(int, input().split())
    numB = Ac[B]
    ans += (C - B) * numB
    print(ans)
    Ac[C] += numB
    Ac[B] = 0
