N=int(input())
l = [input() for _ in range(N)]

def ans115(N:int,l:list):
    l=sorted(map(int,l))
    count=0
    for i in range(0,N-1):
        count+=l[i]
    return(int(count+l[N-1]*0.5))

print(ans115(N,l))
