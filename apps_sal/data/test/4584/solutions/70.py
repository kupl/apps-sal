n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n - 1):
    b[a[i] - 1] += 1
for j in range(len(b)):
    print(b[j])
