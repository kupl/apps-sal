n = int(input())
X = list(map(int, input().split()))
x_min = min(X)
x_max = max(X)

min_val = 10**6 + 1

for i in range(x_min, x_max + 1):
    min_val = min(min_val, sum(map(lambda x: (x-i)**2, X)))

print(min_val)
