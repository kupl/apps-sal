from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
counta = Counter(a)
countb = Counter(b)
ab = [0] * n
for i in range(n):
    if a[i] == b[i]:
        ab[i] = a[i]

test = set(list(range(1, n + 1)))
for i in range(n):
    setab = set(ab)
    realtest = test - setab

    if ab[i] == 0:
        if a[i] in setab and b[i] in setab:
            if len(realtest) != 0:
                ab[i] = realtest.pop()

        elif a[i] in setab:
            ab[i] = b[i]
        elif b[i] in setab:
            ab[i] = a[i]
        else:
            if counta[a[i]] > 1 and countb[b[i]] > 1:
                if len(realtest) != 0:
                    ab[i] = realtest.pop()
                else:
                    ab[i] = a[i]
            elif counta[a[i]] > 1 and not countb[b[i]] > 1:
                ab[i] = b[i]
            elif not counta[a[i]] > 1 and countb[b[i]] > 1:
                ab[i] = a[i]

print(" ".join(list(map(str, ab))))
