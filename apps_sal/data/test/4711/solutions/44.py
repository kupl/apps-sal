a, b, c = map(int,input().split())

max_bell = max(a,b,c)
print(a + b + c - max_bell)
