r = lambda: list(map(int,input().split()))
n,m = r()
check = lambda x: x[0]/x[1]

print (min(check(r()) for x in range(n)) * m)
