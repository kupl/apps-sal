n,k = map(int, input().split())

# red = 2
# g = 5
# b = 8
r = (n*2+k-1)//k
g = (n*5+k-1)//k
b = (n*8+k-1)//k
print (r+b+g)
