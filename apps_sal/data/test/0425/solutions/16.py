from math import log2
n, p = input().split()
n = int(n)
p = int(p)
k = 1
u = 1
while n - p * k >= 1:
    # print(bin(n-p*k).count('1'),bin(n-p*k),k,log2(n-p*k))
    if log2(n - p * k) + 1 >= k >= bin(n - p * k).count('1'):
        print(k)
        u = 0
        break
    else:
        k += 1
# print(bin(n-p*k).count('1'),bin(n-p*k))
# if log2(n-p*k)>=k:
if u:
    print(-1)
