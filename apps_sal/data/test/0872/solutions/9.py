n=int(input())
l=list(map(int,input().split()))
if min(k%2 for k in l)==max(k%2 for k in l) :
    print(' '.join(map(str,l)))
else:
    print(' '.join(map(str,sorted(l))))

