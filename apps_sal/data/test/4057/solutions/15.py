n = int(input())
a = list(map(int, input().split()))
k = [0] * 200
for i in range(n):
    k[a[i]] += 1
print(max(k))
