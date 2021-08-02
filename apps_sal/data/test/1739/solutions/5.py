n, x = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
sx = sum(arr)
adds = [sx - i for i in arr]
adds.sort()
while adds.count(adds[0]) % x == 0:
    ct = adds.count(adds[0])
    addsok = ct // x
    adds = [adds[0] + 1] * addsok + adds[ct:]

print(pow(x, min(min(adds), sx), (10**9 + 7)))
