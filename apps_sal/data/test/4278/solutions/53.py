from collections import defaultdict
N = int(input())
charl = []
ans = 0
for _ in range(N):
    charl.append(''.join(sorted(input())))
anad = defaultdict(int)
for char in charl:
    anad[char] += 1
for anadv in anad.values():
    if anadv > 1:
        ans += anadv * (anadv - 1) // 2
print(ans)
