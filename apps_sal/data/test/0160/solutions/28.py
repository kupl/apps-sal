import numpy as np

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n, k = map(int,input().split())
a = list(map(int,input().split()))

asum = sum(a)
adiv = make_divisors(asum)
adiv.reverse()

a = np.array(a)
ans = 1
flg = False
for i in adiv:
    a_ = np.sort(a % i)
    # print(i, a_)
    msum = a_.sum()
    msum_ = 0
    for j in range(-1, -n-1, -1):
        msum -= a_[j]
        msum_ += i - a_[j]
        if msum_ > k:
            break
        if msum < msum_:
            break
        if msum == msum_ :
            ans = i
            flg = True
            break
    if flg:
        break

print(ans)
