a = list(map(int, input().split()))
k = int(input())
b = max(a)
for i in range(k):
    b *= 2
print(sum(a) - max(a) + b)
