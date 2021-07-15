x, y, z = map(int,input().split())

def swap(a, b, c):
    i = 0
    i = a
    a = b
    b = i

    i = a
    a = c
    c = i
    print(a,b,c)

swap(x,y,z)
