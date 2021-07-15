n = int(input())
a = list(map(int, input().split()))
sumspref = [a[0]]
for i in range(1, n):
    sumspref.append(sumspref[-1] + a[i])
sums = []
for i in range(n):
    for j in range(i, n):
        sums.append(abs(180 - (sumspref[j] - sumspref[i])))
print(min(sums) * 2)
    


