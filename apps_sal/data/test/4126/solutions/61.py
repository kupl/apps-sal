S = input()
T = ""
U = ""
N = len(S)
for i in range((N-1)//2):
    T += S[i]
for i in range(((N-1)//2)-1,-1,-1):
    U += T[i]
if(T==U):
    if(S == T+S[(N-1)//2]+T):
        print("Yes")
        return
print("No")
