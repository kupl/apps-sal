from math import factorial
n, m, k = list(map(int, input().split()))
if k == 0:
    print(m)
else:
    try:
        print(m*(m-1)**k*(factorial(n-1)//(factorial(k)*factorial(n-k-1))) % 998244353)
    except:
        print(0)

