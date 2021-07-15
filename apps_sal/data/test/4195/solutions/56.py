D, N = map(int, input().split())
'''
q = (N-1)//99
print((100*q + N - 99*q)* 100**D)
'''

if N == 100:
    print(100**D*(N+1))
else:
    print(100**D*N)
