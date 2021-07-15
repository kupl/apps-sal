from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    p,f = map(int,input().split())
    ns,na = map(int,input().split())
    s,a = map(int,input().split())
    wynik = 0
    for ps in range(ns+1):
        if ps*s > p:
            continue
        pa = (p-ps*s)//a
        pa = min(pa,na)
        pozs = ns - ps
        poza = na - pa
        if s > a:
            fa = f//a
            fa = min(fa,poza)
            fs = (f-fa*a)//s
            fs = min(fs, pozs)
        else:
            fs = f//s
            fs = min(fs,pozs)
            fa = (f-fs*s)//a
            fa = min(fa,poza)
        wynik = max(wynik, fa+fs+pa+ps)
    print(wynik)
