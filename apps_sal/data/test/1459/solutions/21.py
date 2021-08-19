n = int(input())
d = list(map(int, input().split()))
(s, t) = list(map(int, input().split()))
op1 = op2 = 0
i = s - 1
while i != t - 1:
    op1 += d[i]
    i = (i + 1) % n
j = t - 1
while j != s - 1:
    op2 += d[j]
    j = (j + 1) % n
print(min(op1, op2))
