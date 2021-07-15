S = input()
K = int(input())


for i in range(K):
    if S[i] != "1":
        print(S[i])
        break
    if i == K-1:
        print(S[K-1])
