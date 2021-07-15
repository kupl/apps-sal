N = int(input())
S = input()

ans = S
count = 0

for i in range(N):
    if(S[i] == "("):
        count += 1
    else:
        count -= 1
    
    if(count<0):
        ans = "(" + ans
        count += 1

count = 0

for i in range(N-1,-1,-1):
    if(S[i] == "("):
        count += 1
    else:
        count -= 1

    if(count>0):
        ans = ans + ")"
        count -= 1

print(ans)

