S = input()
T = input()

ls = len(S)
lt = len(T)
left = -1

for i in range(ls - lt + 1):
    for j in range(lt):
        if S[i + j] != "?" and S[i + j] != T[j]:
            break
    else:
        left = i
if left == -1:
    ans = "UNRESTORABLE"
else:
    ans = S[:left] + T + S[left + lt:]
    ans = ans.replace("?", "a")
print(ans)
