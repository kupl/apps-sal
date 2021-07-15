n, x = list(map(int, input().split()))
a = []
for i in range(n):
    a.insert(i, int(input()))
x_rem = x - sum(a)
m = x_rem // min(a)
print(n + m)
