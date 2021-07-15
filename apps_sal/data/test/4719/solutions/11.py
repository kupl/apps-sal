n = int(input())
A = list("abcdefghijklmnopqrstuvwxyz")
B = [50]*26
for i in range(n):
    C = [0]*26
    s = input()
    s = sorted(s)
    for j in range(len(s)):
        for k in range(26):
            if s[j] == A[k]:
                C[k] += 1
                break
    for m in range(26):
        B[m] = min(B[m],C[m])

D = [] 
for i in range(26):
    D.append(A[i]*B[i])
D.sort()
print(*D, sep = "")
