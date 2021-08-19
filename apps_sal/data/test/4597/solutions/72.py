n = int(input())
f = 1
m = 10 ** 9 + 7
for i in range(1, n + 1):
    f = f % m * i
print(f % m)
