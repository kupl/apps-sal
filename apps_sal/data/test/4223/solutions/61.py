N = int(input())
S = input()
S = list(S)
color = [0]
j = 0
for i in range(1,N) :
    if S[i-1] == S[i] :
        color.append(j)
    else :
        j += 1
        color.append(j)

print(len(set(color)))
