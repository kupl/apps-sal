K=int(input())
S=input()
if len(S)<=K:
    print(S)
else:
    for i in range(K):
        print(S[i],end="")
    print("...")
