N,X,T = map(int, input().split())

print(N//X*T) if N%X==0 else print(T*(N//X+1))
