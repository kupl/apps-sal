S = str(input())
T = str(input())
ans_list = []

for i in range(len(S)):
    i = S[-1] + S[0:-1]
    ans_list.append(i)
    S = i

if T in ans_list:
    print("Yes")
else:
    print("No")
