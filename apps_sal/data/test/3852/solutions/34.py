n = int(input())
A = list((int(x) for x in input().split()))
minimum = min(A)
maximum = max(A)
ANS = []
if abs(maximum) >= abs(minimum):
    index = A.index(maximum)
    for i in range(n):
        ANS.append((index, i))
    for i in range(n - 1):
        ANS.append((i, i + 1))
else:
    index = A.index(minimum)
    for i in range(n):
        ANS.append((index, i))
    for i in reversed(list(range(1, n))):
        ANS.append((i, i - 1))
print(len(ANS))
for (x, y) in ANS:
    print((x + 1, y + 1))
