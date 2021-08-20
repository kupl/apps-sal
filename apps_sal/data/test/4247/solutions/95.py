a = input()
n = int(a)
p = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if p[i - 1] < p[i] and p[i] <= p[i + 1] or (p[i + 1] < p[i] and p[i] <= p[i - 1]):
        count = count + 1
print(count)
