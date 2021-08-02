n = int(input())
x = sorted(map(int, input().split()))
a = 0
for i in range(n // 2):
    a += (x[i] + x[n - i - 1])**2
print(a)
