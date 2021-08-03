n = int(input())

arr = list(map(int, input().split()))
arr.sort()

a = []
for t in range(1, 101):
    tot = 0
    for item in arr:
        if (abs(item - t) >= 1):
            tot += abs(item - t) - 1

    a.append((tot, t))

a.sort()

print(a[0][1], a[0][0])
