N = int(input())
A = list(map(int, input().split()))
order = []
for (n, a) in enumerate(A):
    order.append([n + 1, a])
order.sort(key=lambda x: x[1])
for (Num, num) in order:
    print(Num, end=' ')
print()
