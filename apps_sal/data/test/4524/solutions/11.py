n, m = [int(i) for i in input().split()]
a = input()
b = input()
if m < n:
    m = n
    b = ('0'*(m-len(b)))+b
elif n < m:
    n = m
    a = ('0'*(n-len(a)))+a

ones_left = [0]*m
if b[0] == '1':
    ones_left[0] = 1
    
for i in range(1, n):
    ones_left[i] = ones_left[i-1]
    if b[i] == '1':
        ones_left[i] += 1

ans = 0
k = 0
mod = 998244353
for i in range(n):
    k = 1 if a[i] == '1' else 0
    ans += k*pow(2, n-1-i, mod)*ones_left[i]
    ans %= mod
    
print(ans)
