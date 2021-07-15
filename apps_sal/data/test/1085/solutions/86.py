n = int(input())
from numpy import sqrt
cnt = 2
rt = int(sqrt(n))
for i in range(2,rt+1):
    if n % i == 0:
        m = n
        while m%i ==0:
            m = m//i
        if m%i == 1:
            cnt += 1
    elif (n-1) % i ==0:
        cnt += 2
if n == rt ** 2 + 1:
    cnt -= 1
print(cnt)
