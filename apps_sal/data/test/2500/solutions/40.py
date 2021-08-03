# coding: utf-8
# Your code here!
odd = {0: 1}
even = {0: 1, 1: 3}
M = 10**9 + 7


def memo(N):
    if N == 0:
        return 1
    if N == 1:
        return 2
    return (memoodd((N - 1) // 2) + memoeven(N // 2)) % M


def memoodd(N):
    if N in odd:
        return odd[N]
#    a=memoodd((N-1)//2)
#    b=memoeven(N//2)
    odd[N] = memo(N)
    return odd[N]


def memoeven(N):
    if N in even:
        return even[N]
#    a=memoodd((N-1)//2)
#    b=memoeven(N//2)
#    c=memoodd((N-2)//2)
#    d=memoeven((N-1)//2)
#    return a+b+c+d
    even[N] = (memo(N) + memo(N - 1)) % M
    return even[N]


n = int(input())

print((memo(n)))
