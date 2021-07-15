N = int(input())
S,T = map(str,input().split())
U = []
for i in range(N):
    U.append(S[i])
    U.append(T[i])
print("".join(U))
