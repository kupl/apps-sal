n = int(input())

a = list(map(int, input().split()))

dead = 0
i = n - 1
change = 1
while i >= 0:
    change -= 1
    if change > 0:
        dead += 1
    change = max(change, a[i] + 1)
    i -= 1

print(n - dead)
