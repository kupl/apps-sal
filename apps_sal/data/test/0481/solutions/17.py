__author__ = 'User'
n, x = list(map(int, input().split()))
c = 0
#print(x // n)
for i in range(max(1, x // n), n + 1):
    if x % i == 0 and x // i <= n:
        #print(i)
        c += 1
print(c)

