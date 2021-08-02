k, p = list(map(int, input().strip().split()))


vsota = 0

count = 0

x = 1
while True:
    u = int(str(x) + str(x)[::-1])
    vsota += u
    count += 1
    if count == k:
        break
    x += 1
print(vsota % p)
