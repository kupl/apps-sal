(n, k) = list(map(int, input().split()))
A = [int(x) for x in input().split()]
A.append(-1)
s = input() + '$'
dmg = 0
lc = None
count = 0
atk = []
for i in range(n + 1):
    c = s[i]
    a = A[i]
    if c != lc:
        if lc:
            dmg += sum(sorted(atk)[-k:])
        count = 0
        atk = []
    count += 1
    lc = c
    atk.append(a)
print(dmg)
