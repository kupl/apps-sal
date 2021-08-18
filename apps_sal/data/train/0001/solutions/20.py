q = int(input())
for i in range(q):
    n, m, k = map(int, input().split())
    ost = max(n, m) - min(n, m)
    plus = 0
    if ost % 2 != 0:
        plus = 1
        ost -= 1
    mini = min(n, m) + ost + plus
    if k < mini:
        print(-1)
    elif (k - mini) % 2 == 0 or plus == 1:
        print(k - plus)
    else:
        print(k - plus - 2)
