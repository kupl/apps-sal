n, s = list(map(int, input().split()))
v = [int(k) for k in input().split()]
v.sort(reverse=True)
for i in range(n):
    s -= v[i] - v[-1]
    v[i] = v[-1]
if s <= 0:
    print(v[-1])
else:
    if s > n * v[0]:
        print(-1)
    else:
        print(v[0] - (s + n - 1) // n)  

