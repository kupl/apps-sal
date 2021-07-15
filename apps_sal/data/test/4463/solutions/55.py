s = input()
t = input()
S = sorted(s)
T = sorted(t,reverse=True)
#print(S,T)
ans = "W"
for i in range(min(len(s),len(t))):
    if S[i] > T[i]:
        ans = "No"
        break
    elif ans == "W" and S[i] == T[i]:
        ans = "W"
    elif ans == "W" and S[i] < T[i]:
        ans = "Yes"
        break
if ans == "W":
    if len(s) < len(t):
        ans = "Yes"
    else:
        ans = "No"
print(ans)
