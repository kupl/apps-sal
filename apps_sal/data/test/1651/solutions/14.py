f = 0
(S, P) = map(int, input().split())
x = int(P ** 0.5)
for i in range(1, x + 1):
    if P % i == 0 and P // i + i == S:
        f = 1
print('Yes' if f == 1 else 'No')
