n = int(input())
m = 0
a = 1
p = 0
l = list(map(int, input().split()))
for i in range(n):
    if l[i] == 1:
        m += 1
        if m > 0:
            if m > 1:
                a *= i - p
            p = i
print(a if m > 0 else 0)
