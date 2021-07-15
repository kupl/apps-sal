from collections import defaultdict
N = int(input())
prm = defaultdict(int)
for n in range(2, N+1):
    for p in range(2, int(n**0.5)+2):
        while n % p == 0:
            prm[p] += 1
            n //= p
        if n == 1:
            break
    else:
        prm[n] += 1
C = [2, 4, 14, 24, 74]
cnt = [0]*5
for p, x in list(prm.items()):
    for i, c in enumerate(C):
        if x >= c:
            cnt[i] += 1
c2, c4, c14, c24, c74 = cnt

ans = c4*(c4-1)//2*(c2-2) if c2 > 2 else 0
ans += max(0, c24*(c2-1))
ans += max(0, c14*(c4-1))
ans += c74
print(ans)

