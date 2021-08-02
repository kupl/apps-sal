n = int(input())
a = [0] * (n + 1)
for i in range(n + 1):
    if i % 3 == 0 or i % 5 == 0:
        a[i] = 0
    else:
        a[i] = i
print(sum(a))
