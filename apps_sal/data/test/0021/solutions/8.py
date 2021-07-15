n=int(input())
l=list(map(int,input().split()))
mi=l.index(1)+1
ma=l.index(n)+1
print(max(abs(mi-1),abs(mi-n),abs(ma-1),abs(ma-n)))
