import sys


def check(pay, like):
    str_pay = str(pay)
    like = ''.join(like)
    for p in str_pay:
        for lk in like:
            if p == lk:
                return False

    return True

N, K = list(map(int, input().split()))

D = []
D = list(map(int, input().split()))
str_D = []

for s in D:
    str_D.append(str(s))

pay = N

while True:
    if check(pay, str_D):
        print(pay)
        return
    pay += 1

