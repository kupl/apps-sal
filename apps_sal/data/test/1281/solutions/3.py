from collections import defaultdict
(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
xors = defaultdict(int)
xors[0] = 1
comp = (1 << k) - 1
ans = n * (n + 1) // 2
xor = 0
for a in arr:
    xor ^= a
    if xors[xor] > xors[comp ^ xor]:
        xor ^= comp
    ans -= xors[xor]
    xors[xor] += 1
print(ans)
