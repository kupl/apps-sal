S = input()
T = input()

n = len(S)+1
while n:
    S = S[-1] + S[:-1]
    if S == T:
        print("Yes")
        return
    n -= 1
print("No")
