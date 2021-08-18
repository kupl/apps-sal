n = int(input())
x = list(map(int, input().split()))
sum = 1000000000000000
for p in range(1, 101):

    tmp = 0
    for i in range(len(x)):
        tmp += (x[i] - p)**2
    sum = min(sum, tmp)
print(sum)
