k = int(input())
t = 7
t %= k

for i in range(k + 1):
    if t == 0:
        print((i + 1))
        break
    t = (t * 10 + 7) % k
else:
    print((-1))
