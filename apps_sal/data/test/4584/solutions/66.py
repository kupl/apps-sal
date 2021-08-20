n = int(input())
w = list(map(int, input().split()))
a = [0] * n
for i in range(n - 1):
    a[w[i] - 1] += 1
for j in range(n):
    print(a[j])
