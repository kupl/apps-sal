n=int(input())
S=str(input())
r=S.count('R')
g=S.count('G')
b=S.count('B')
cnt=r*g*b

for j in range(2, n, 2):
    for i in range(0, n-j):
        k = (2 * i + j) // 2
        if S[i] != S[i+j] and S[i] != S[k] and S[k] != S[i+j]:
            cnt -= 1

print(cnt)
