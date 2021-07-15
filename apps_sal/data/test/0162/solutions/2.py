n, k =list(map(int, input().split()))
a = list(map(int, input().split()))
m = 0
for i in a:
    if k % i == 0:
        m = max(m, i)
print(k//m)

