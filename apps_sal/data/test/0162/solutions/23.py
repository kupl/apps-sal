n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
m = 1
for i in l:
    if k % i == 0:
        m = max(m, i)
print(k // m)
