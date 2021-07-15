
n = int(input())
l = list(map(int, input().split()))

a = [0] * (n + 1)
k = 0

for x in l:
    a[x] = a[x - 1] + 1
    k = max(k, a[x])    

print(n - k)

