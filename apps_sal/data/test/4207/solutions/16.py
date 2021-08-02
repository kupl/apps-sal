def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]

pre = 0
for ai, bi in zip(a, b):
    if (ai, bi) == (0, 0):
        pre += 1

fracs = [(-bi // gcd(ai, bi), ai // gcd(ai, bi)) if ai !=
         0 else float('inf') for ai, bi in zip(a, b)]

cnt = {item: 0 for item in fracs}

for x in fracs:
    if x != float('inf'):
        cnt[x] += 1

print(max(cnt.values()) + pre)
