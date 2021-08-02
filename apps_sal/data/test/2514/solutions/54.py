from collections import Counter

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]

cou = Counter(a)
s = sum(a)

for b, c in bc:
    s = s + cou[b] * (c - b)
    cou[c] += cou[b]
    cou[b] = 0
    print(s)
