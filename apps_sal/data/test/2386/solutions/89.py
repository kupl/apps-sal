import statistics
n = int(input())
x = list(map(int, input().split()))
value = 0
for _ in range(n):
    x[_] -= _ + 1
x.sort()
for _ in x:
    value += abs(_ - x[n // 2])
print(value)
