N=int(input())
S=input()
x="Yes"
if N%2==1:
    print("No")
else:
    for i in range(0,N//2):
        if S[i]!=S[i+N//2]:
            x="No"
            break
    print(x)
