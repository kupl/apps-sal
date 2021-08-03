n = int(input())
mas1 = list(map(int, input().split(" ")))
mas2 = list(map(int, input().split(" ")))
mas3 = list(map(int, input().split(" ")))
sum1 = 0
sum2 = sum(mas2)
res = list()
for i in range(n):
    res.append(sum1 + sum2 + mas3[i])
    if i < n - 1:
        sum2 -= mas2[i]
        sum1 += mas1[i]
res.sort()
print(res[0] + res[1])
