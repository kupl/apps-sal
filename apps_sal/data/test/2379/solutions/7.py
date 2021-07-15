N, K, C = map(int, input().split())
S = input()[::-1]
Top = []
Bottom = []
yasumi = 0
ans = []
k = K
for i in range(N):
    if (yasumi == 0) and (S[i] == "o") and (k > 0):
        Bottom.append(N-i)
        yasumi += C
        k -= 1
    elif yasumi > 0:
        yasumi -= 1

S_ = S[::-1]
Bottom.sort()
j = -1
yasumi = 0
for i in range(N):
    if (yasumi == 0) and (S_[i] == "o") and (K > 0):
        j += 1
        yasumi += C
        K -= 1
        if j >= len(Bottom):
            break
        elif Bottom[j] == i+1:
            ans.append(i+1)
    elif yasumi > 0:
        yasumi -= 1

for i in ans:
    print(i)
