m = int(input())
k = 0
num = 0
mem = 0
r = 0
while k < m + 1:
    num += 1
    n = num
    while n > 1 :
        if n % 5 == 0:
            r += 1
            n //= 5
        else:
            break
    mem = k
    k += r
    r = 0
if (mem - m != 0):
    print(0)
else:
    print(5)
    print(' '.join(map(str, list(range(num-5, num)))))

