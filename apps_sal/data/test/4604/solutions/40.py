n = int(input())
a = list(map(int, input().split()))

from collections import Counter
c = Counter(a)

check_ary = []
if n&1:
    check_ary.append(0)

for i in range(n//2):
    for _ in range(2):
        check_ary.append((i+1)*2 if n&1 else i*2+1)

c2 = Counter(check_ary)

if c != c2:
    print(0)
    return

print(pow(2, n//2, 10**9+7))
