import math
from functools import reduce
N = int(input())
A = list(map(int, input().split()))
A.sort()
MAXN = A[-1]
sieve = [1] * (MAXN + 1)
st = set()
for a in A:
    if a in st:
        sieve[a] = 0
    if sieve[a] == 1:
        for q in range(2 * a, MAXN + 1, a):
            if sieve[q] == 1:
                sieve[q] = 0
    st.add(a)
ans = 0
for a in A:
    ans += sieve[a]
print(ans)
