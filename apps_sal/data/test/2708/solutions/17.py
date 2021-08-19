# cook your dish here
n, k = list(map(int, input().split()))
nn = str(n)
while(k):
    if(nn[-1] != '0'):
        n -= 1
        nn = str(n)
    else:
        n = n // 10
        nn = str(n)
    k -= 1
print(n)
