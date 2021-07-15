a,b = map(int,input().split())
L = [str(a)*b, str(b)*a]


L = sorted(L)
print(L[0])
