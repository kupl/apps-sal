(n, k) = map(int, input().split())
l = list(map(int, input().split()))
t = 0
for i in range(n):
    if t + i + 1 >= k:
        break
    else:
        t += i + 1
print(l[k - t - 1])
