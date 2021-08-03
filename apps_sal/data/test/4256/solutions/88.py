a, b, c = list(map(int, input().split()))
myans1 = int(b / a)
if(myans1 > c):
    print(c)
else:
    print(myans1)
