A,B,C,D=map(int,input().split())
start=max(A,C)
end=min(B,D)

print(end-start if end-start>0 else 0)
