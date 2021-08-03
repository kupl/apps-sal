n = int(input())
l = [int(i) for i in input().split(" ")]
p = [int(i) for i in input().split(" ")]
sum1 = 0
sum2 = 0
a = max(p)
b = min(p)
sum1 += sum(l[b - 1:a - 1])
sum2 += sum(l) - sum1
print(min(sum1, sum2))
