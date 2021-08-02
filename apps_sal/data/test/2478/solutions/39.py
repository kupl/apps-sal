import copy
N = int(input())
S = list(input())
S_ans = copy.deepcopy(S)
app = 0
q = [0]
save = 0
for i in range(N):
    if S[i] == '(':
        q.append(q[-1] + 1)

    else:
        q.append(q[-1] - 1)
        if q[-1] == -1:
            S_ans.insert(app + save, "(")
            app += 1
            q[-1] = 0

for i in range(q[-1]):
    S_ans.append(")")
print("".join(S_ans))
