n = int(input())
l = list(map(int, input().split()))
m = [0 for i in range(11)]
wyn = 0
for i in range(n):
    m[l[i]] += 1
    b = [m[i] for i in range(11) if m[i] != 0]
    b = sorted(b)
    if len(b) == 1:
        wyn = i + 1
    if len(b) > 1:
        if b[0] == 1 and sum(b) == 1 + len(b) * b[1] - b[1]:
            wyn = i + 1
        elif b[0] == b[-2] and b[-1] == b[0] + 1:
            wyn = i + 1
print(wyn)
