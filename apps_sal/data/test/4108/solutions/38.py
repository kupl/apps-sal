S = input()
T = input()
N = len(S)
count = 0
R_1 = [-1 for i in range(26)]
R_2 = [-1 for i in range(26)]

answer = "Yes"
for i in range(N):
    r1 = ord(S[i]) - 97
    r2 = ord(T[i]) - 97
    if R_1[r1] >= 0:
        if r2 != R_1[r1]:
            answer = "No"
            break
    if R_2[r2] >= 0:
        if r1 != R_2[r2]:
            answer = "No"
            break
    if R_1[r1] < 0:
        R_1[r1] = r2
    if R_2[r2] < 0:
        R_2[r2] = r1
print(answer)
