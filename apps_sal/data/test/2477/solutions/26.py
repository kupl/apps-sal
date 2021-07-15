N, K = list(map(int, input().split()))
*A, = list(map(int, input().split()))

def f(t):
    if t!=0:
        c = 0
        for i in A:
            c += i//t if i!=t else 0
        return c<=K
    else:
        return all(i<=t for i in A)

left, right = -1, 10**10
while right-left>1:
    m = (right+left)//2
    if f(m):
        right = m
    else:
        left = m

print(right)

