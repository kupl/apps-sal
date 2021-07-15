K=int(input())
S=input()
if K>=len(S):
    print(S)
else:
    for i in range(K):
        print(S[i],end='')
    print("...")
