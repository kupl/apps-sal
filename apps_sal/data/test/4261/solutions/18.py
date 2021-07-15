a,b,c = map(int, input().split())

n = a - b
if c < n:
    print(0)
else:
    print(c - n)
