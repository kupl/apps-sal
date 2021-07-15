def inl():
    l = list(map(int , input().split()))
    return l

x , y = map(int , input().split())
l = 0
while 1:
    x *= 3
    y *= 2
    l += 1
    if(x > y):
        print(l)
        break
