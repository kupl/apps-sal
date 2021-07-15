n, k = map(int, input().split())

res = 0
for i in range(1, n + 1):
    a = i % k
    b = (-a) % k
    c = (-a) % k
    if (b + c) % k == 0:
        res += ((n + b) // k) * ((n + c) // k)
        
print(res)
