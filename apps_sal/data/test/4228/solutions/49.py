#ABC131 B

N,L = map(int,input().split())
aji = []
for i in range(N):
    aji.append(L+i)
if L < 0 and L+N-1 > 0:
    print(sum(aji))
elif L+N-1 <= 0:
    print(sum(aji) - (L+N-1))
elif L >= 0:
    print(sum(aji) - L)
