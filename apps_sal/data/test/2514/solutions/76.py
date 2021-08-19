import collections
N = int(input())
A = list(map(int, input().split()))
Ac = collections.Counter(A)
ans = sum(A)
Q = int(input())
Ackey = set(Ac.keys())
for _ in range(Q):
    (B, C) = list(map(int, input().split()))
    if B in Ackey:
        numB = Ac[B]
    else:
        numB = 0
    ans += (C - B) * numB
    print(ans)
    Ac[C] += numB
    Ackey.add(C)
    Ac[B] = 0
