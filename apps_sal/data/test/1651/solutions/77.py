S, P = map(int, input().split())
a = 0
for i in range(1, min(10**6, S // 2) + 1):
    if i * (S - i) == P:
        a += 1
if a == 0:
    print('No')
else:
    print('Yes')
