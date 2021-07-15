n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(100)]
for i in range(n):
    b[a[i] - 1] += 1
print(max(b))
