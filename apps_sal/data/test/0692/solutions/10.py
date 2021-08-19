def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


input()
m = list(map(int, input().split()))
r = list(map(int, input().split()))
result = 1
for mod in m:
    result = result * mod // gcd(result, mod)
good = 0
for i in range(result):
    for (mod, car) in zip(m, r):
        if i % mod == car:
            good += 1
            break
print(good / result)
