r,d,x = map(int,input().split())

weight = x

for i in range(10):
    weight = r*weight-d
    print(weight)
