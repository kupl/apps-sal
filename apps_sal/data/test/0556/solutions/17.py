l, r, n = [int(x) for x in input().split()]

f = 1
count = 0
while f <= r:
    if f >= l:
        print(f, end=" ")
        count += 1

    f *= n

if count == 0:
    print(-1)
