S = input()
N = len(S)

def f(k):
    s = S[-k:k]
    if s == "":return False
    return s.count(s[0])!=len(s)

def binary_search(l,r,func):
    if func(l):return l-1
    if not func(r):return r
    while l+1<r:
        i = (l+r)//2
        if func(i):
            r = i
        else:
            l = i
    return l

print(binary_search(0,N,f))
