from math import log
def ii(): return int(input())
def kk(): return map(int, input().split())
def ll(): return list(kk())


elems = [0] * 126
n, k = kk()
c = 0
for i in range(63):
    if n & (2**i):
        elems[i] = 1
        c += 1
if c > k:
    print("No")
    return
for i in range(63, -63, -1):
    if elems[i]:
        if elems[i] > k - c:
            # stop it, now reverse sweep
            break
        c += elems[i]
        elems[i - 1] += elems[i] * 2
        elems[i] = 0
prin = []
for i in range(63, -63, -1):
    prin.extend([i] * elems[i])
while len(prin) < k:
    prin[-1] -= 1
    prin.append(prin[-1])
print("Yes")
print(" ".join(map(str, prin)))
