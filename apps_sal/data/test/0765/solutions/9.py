(T, S, q) = [int(i) for i in input().split(' ')]
res = 1
loaded = S
while loaded * q < T:
    loaded = loaded * q
    res += 1
print(res)
