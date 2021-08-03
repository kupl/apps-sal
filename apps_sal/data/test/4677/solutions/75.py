S = str(input())

ans = []
for i in range(len(S)):
    if S[i] == "B":
        if ans == []:
            continue
        else:
            ans = ans[:-1]
    else:
        ans.append(S[i])
    # print(ans)
# print(ans)

for i in range(len(ans)):
    print(ans[i], end="")
