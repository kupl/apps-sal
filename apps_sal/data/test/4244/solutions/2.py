n = int(input())
x = list(map(int, input().split()))
p = sum(x) // n
e1 = 0
e2 = 0
for i in x:
    e1 += (p - i) ** 2
    e2 += (p + 1 - i) ** 2
print(min(e1, e2))
