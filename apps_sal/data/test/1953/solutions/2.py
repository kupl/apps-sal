n = int(input())
ar = list(sorted(list(map(int, input().split()))))
curr = 0
sum1 = 0
for i in range(n):
    if curr <= ar[i]:
        sum1 += 1
        curr += ar[i]
print(sum1)
