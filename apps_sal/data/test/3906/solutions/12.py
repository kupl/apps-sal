
# coding: utf-8

# In[7]:

n, m = list(map(int, input().split()))

def fib(n):
    if n<2:
        return 1
    a = 1
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

print((2*fib(n)+2*fib(m)-2)%(10**9+7))


