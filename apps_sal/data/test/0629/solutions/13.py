n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
p1 = [0]
for i in range(n - 1):
    p1.append(p1[-1] + a[i])
p2 = [0]
for i in range(n - 1):
    p2.append(p2[-1] + b[-i - 1])
min1 = 10000000
min2 = 10000000
for i in range(n):
    summ = p1[i] + p2[n - i - 1] + s[i]
    if summ < min1:
        min2 = min1
        min1 = summ
    elif summ < min2:
        min2 = summ
print(min1 + min2)
