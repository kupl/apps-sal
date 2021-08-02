n = int(input())
a = list(map(int, input().split()))
c = a[n - 1]
k = n - 1
t = 0
while a[k] == c:
    t += 1
    k -= 1
print(n - t)
