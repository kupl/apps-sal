n = int(input())
l = list(map(int, input().split()))
l.sort()
sum = 0
if n != 1:
    for i in range(2, n + 1):
        sum += i * l[i - 2]
    sum += n * l[n - 1]
    print(sum)
else:
    print(l[0])
