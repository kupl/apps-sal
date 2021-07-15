from math import log2
n = int(input())
if n == 1:
    print(1)
    return
elif n == 3:
    print(1, 1, 3)
    return
l = [1] * (n // 2)
if n % 2 == 1:
    l.append(1)

xn = int(log2(n))
tmp = n - len(l)
for i in range(2, xn+1):
    fn = tmp // 2
    if tmp % 2 == 1:
        fn += 1
    tmp -= fn
    l += ([pow(2, i-1)] * fn)
l.append((n // pow(2, xn - 1)) * pow(2, xn - 1))
print(' '.join(str(i) for i in l))
