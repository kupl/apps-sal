n = int(input())
k = 0
v = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(n):
    if v[i] - c[i] > 0:
        k += v[i] - c[i]
print(k)
