import sys
input = sys.stdin.readline

def find_ok( x , Oks ):
    for i in Oks:
        if int(i) > int(x):
            break
    return i

def main():
    n,k = map( int , input().split() )
    Nos = set(map( int , input().split() ))
    while(1):
        x = str(n)
        set_n= set()
        for digit in x:
            set_n.add( int(digit) )
        if len(set_n & Nos) == 0:
            break
        n += 1
    print(n)



main()
