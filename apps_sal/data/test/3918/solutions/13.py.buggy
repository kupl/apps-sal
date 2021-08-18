n, k1, k2 = [int(x)for x in input().split()[:3]]
ks1 = [int(x) for x in input().split()[:n]]
ks2 = [int(x) for x in input().split()[:n]]
err = [abs(ks1[i] - ks2[i]) for i in range(n)]
num = k1 + k2
rest1 = False
if num % 2 != sum(err) % 2:
    rest1 = True


def kill():
    nonlocal num
    maxx = max(err)
    if maxx == 0 or num == 0:
        return False
    for i in range(len(err)):
        if err[i] == maxx:
            err[i] -= 1
            num -= 1
            if num == 0:
                return False
    return True


while kill():
    pass
summ = sum([x**2 for x in err])
if summ == 0 and rest1:
    print(1)
else:
    print(summ)
