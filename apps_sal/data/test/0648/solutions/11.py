import sys

def main():
    m,b = list(map(int,sys.stdin.readline().split()))
    
    def calc(y):
        x = (b-y)*m
        return ((y*(y+1)*(x+1))>>1) + ((x*(x+1)*(y+1))>>1)
    
    res = 0
    for i in range(b+1):
        t = calc(i)
        if t>res:
            res = t
    print(res)


main()

