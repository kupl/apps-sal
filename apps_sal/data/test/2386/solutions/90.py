import statistics
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] - (i + 1)

min_sad = float("inf")
b = int(statistics.median(a))
for b_ in range(b - 1, b + 2):
    a_ = [abs(i - b_) for i in a]
    sad = sum(a_)
    min_sad = min(sad, min_sad)

print(min_sad)
