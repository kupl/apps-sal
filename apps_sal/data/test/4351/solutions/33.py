S = input()
N = len(S)

for i in range(N // 2):
    if S[i] != S[-i - 1]:
        print("No")
        break
else:
    print("Yes")
