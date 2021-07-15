N,K = map(int,input().split())
S = str(input())
T = list(map(str,S))

for i in range(N):
    if i == K-1:
        T[i] = str.lower(T[i])

print("".join(T))
