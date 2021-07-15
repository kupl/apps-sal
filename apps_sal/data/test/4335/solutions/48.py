N = int(input())
S = input()
if S[:len(S)//2] == S[len(S)//2:]:
    print("Yes")
else:
    print("No")
