n = int(input())
x = list(map(int, input().split()))
d = float("inf")
for i in range(max(x) + 1):
    c = 0
    for j in range(len(x)):
        c += (x[j] - i)**2
    d = min(c, d)
print(d)
