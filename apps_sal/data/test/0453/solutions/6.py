from sys import stdin
def main():
    x = stdin.readline().strip()
    for i in range (0,len(x)):
        if x[i] == '=':
            b = i
        if x[i] == '+':
            a = i
    c = len(x[0:a])
    d = len(x[b+1:len(x)])
    e = len(x[a+1:b])
    if c+e==d:
        print (x)
    else:
        if c+e > d:
            if c+e > d and c+e != d:
                if(c==1):
                    e-=1
                else:
                    c -= 1
                d += 1
            if d != c+e:
                print ('Impossible')
            else:
                m = ('|'*c,'+','|'*e,'=','|'*d)
                m=''.join(m)
                print(m)
        else:
            if d > c+e and c+e != d:
                d -= 1
                c += 1
            if c+e != d:
                print ('Impossible')
            else:
                n = ('|'*c,'+','|'*e,'=','|'*d)
                n=''.join(n)
                print(n)
        
main()

