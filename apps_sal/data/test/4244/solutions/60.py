N = int(input())
X = list(map(int, input().split()))

total = 0
m = round(sum(X) / N)

for i in X:
    total += (m - i) ** 2
print(total)
