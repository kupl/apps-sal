S = input()
K = int(input())
for i in range(len(S)):
    if S[i] != '1':
        print(S[i])
        break
    elif i + 1 < K and S[i] == '1':
        continue
    else:
        print(1)
        break
