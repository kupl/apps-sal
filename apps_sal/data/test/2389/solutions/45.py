N, A, B, C = list(map(int, input().split()))
vars = {"A": A, "B": B, "C": C}
sum_ABC = A + B + C
S = [input() for _ in range(N)]
Ans = []
for s, s_next in zip(S, S[1:]):
    if vars[s[0]] > vars[s[1]] or (vars[s[0]] == vars[s[1]] and s[1] in s_next):
        Ans.append(s[1])
        vars[s[1]] += 1
        vars[s[0]] -= 1
    else:  # vars[s[0]] < vars[s[1]]:
        Ans.append(s[0])
        vars[s[0]] += 1
        vars[s[1]] -= 1
    if vars[s[0]] < 0 or vars[s[1]] < 0:
        print("No")
        return
s = S[-1]
if vars[s[0]] > vars[s[1]]:
    Ans.append(s[1])
    vars[s[1]] += 1
    vars[s[0]] -= 1
else:
    Ans.append(s[0])
    vars[s[0]] += 1
    vars[s[1]] -= 1
if vars[s[0]] < 0 or vars[s[1]] < 0:
    print("No")
    return
print("Yes")
print(("\n".join(Ans)))
