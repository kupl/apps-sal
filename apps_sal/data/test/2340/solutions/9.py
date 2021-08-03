q = int(input())
for i in range(q):
    h, n = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()] + [10**10]
    counter = 0
    arr = 0
    for i in range(1, n + 1):
        if a[i] == a[i - 1] - 1:
            counter += 1
        else:
            if counter % 2 == 1 and a[i - 1] != 1:
                arr += 1
            counter = 1
    print(arr)
