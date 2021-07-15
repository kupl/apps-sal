def mi():
    return list(map(int, input().split()))
'''
6 9 2
1 3 3 7 4 2
'''
n,m,k = mi()
a = list(mi())
a.sort(reverse=True)
t = k+1
nop = m//t
rem = m%t
print(nop*(k*a[0]+a[1])+rem*a[0])

