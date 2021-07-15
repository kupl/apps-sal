n = int(input())

trees = []
for i in range(n):
    xi, hi = list(map(int, input().split()))
    trees.append((xi, hi))

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    count = 2
    last = trees[0][0]

    for i in range(1, n - 1):
        x, h = trees[i]
        next = trees[i + 1][0]
        if (x - h) > last:
            #print("last", trees[i], last, next)
            count += 1
            last = x
        elif (x + h) < next:
            #print("next", trees[i], last, next)
            count += 1
            last = x + h
        else:
            last = x

    print(count)

