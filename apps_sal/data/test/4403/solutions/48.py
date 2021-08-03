S = input()
ans = 0
for i in range(4):
    if S[i] == "+":
        ans += 1
    elif S[i] == "-":
        ans -= 1

print(ans)
