m, r = list(map(int, input().split()))

def calc(k):
    nonlocal r
    if k < 1:
        return 0
    elif k == 1:
        return r * (2**0.5 + 2)
    else:
        return r * ((1 + 2 * (k - 1)) * 2**0.5 + k * 2 + (k - 1) * (k - 2))

avg = 0
div = m ** 2

for i in range(0, m):
    avg += (2 * r + calc(i) + calc(m - 1 - i)) / div
 
print(avg)

