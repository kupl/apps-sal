n = int(input())
t = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    sum = 0
    count = 1
    (p, x) = list(map(int, input().split()))
    for j in t:
        if p == count:
            sum += x
        else:
            sum += j
        count += 1
    print(sum)
