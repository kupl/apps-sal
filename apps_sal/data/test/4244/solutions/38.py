n = int(input())
x = list(map(int, input().split()))
sum = 1000000000000000
for p in range(1, 101):

    tmp = 0
    # print("p",p)
    for i in range(len(x)):
        tmp += (x[i] - p)**2
        # print("tmp",tmp)
    sum = min(sum, tmp)
    # print("su",sum)
print(sum)
