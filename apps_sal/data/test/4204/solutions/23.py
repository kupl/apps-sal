S = str(input())
K = int(input())
for i in range(K):
    if S[i] != "1":
        break
else:
    while S[i] != "1":
        i += 1
        
print(S[i])
