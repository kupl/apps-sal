from collections import Counter
N, P = map(int, input().split())
S = input()

if P in (2, 5):
    ans = 0
    for i, c in enumerate(S):
        if int(c) % P == 0:
            ans += i + 1
    print(ans)
    return

mem = [0]
j = 1
for c in S[::-1]:
    mem.append((mem[-1] + int(c) * j) % P)
    j *= 10
    j %= P
ctr = Counter(mem)
ans = 0
for v in ctr.values():
    ans += v * (v - 1) // 2
print(ans)
