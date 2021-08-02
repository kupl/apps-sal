S = input()
T = input()
S = S + S

for i in range(0, len(S) - len(T) + 1):
    if S[i: i + len(T)] == T:
        print("Yes")
        return

print("No")
