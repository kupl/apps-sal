N = int(input())
S = input()

if S[:int(N/2)] == S[int(N/2):N]:
    print("Yes")
else:
    print("No")


