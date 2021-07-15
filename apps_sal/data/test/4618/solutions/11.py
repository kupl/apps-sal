S = input()
k = int(input())
abc = []
for i in range(len(S)):
    for j in range(1, k+1):
        if i+j <= len(S):
            s = S[i:i+j]
            if not s in abc:
                abc.append(S[i:i+j])
    
abc = sorted(abc)
print((abc[k-1]))

