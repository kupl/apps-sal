N=int(input())
A=sorted(list(map(int,input().split())))
l=[]
s=set()
for i in range(N):
    if A[N-i-1] in s:
        l.append(A[N-i-1])
        s.discard(A[N-i-1])
    else:
        s.add(A[N-i-1])
l.sort()
print(0 if len(l)<2 else l[-1]*l[-2])
