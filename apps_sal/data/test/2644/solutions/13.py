n = int(input())
p = list(map(int, input().split()))

unswapped = [True] * n
swap_count = 0
swap_order = []
now = 1

for i in range(1, n):
    if p[i] == now:
        for j in range(i, now - 1, -1):
            if unswapped[j]:
                unswapped[j] = False
                swap_count += 1
                swap_order.append(j)
                p[j], p[j-1] = p[j-1], p[j]
            else:
                print(-1)
                return
        now = i + 1

for i in range(n):
    if p[i] != i + 1:
        print(-1)
        return

if swap_count == n - 1:
    print(*swap_order, sep="\n")
else:
    print(-1)
