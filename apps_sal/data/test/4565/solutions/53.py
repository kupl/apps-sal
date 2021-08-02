n = int(input())
s = list(input())
ans = [0] * n
ans[0] += list(s[1:]).count("E")
for i in range(1, n):
    if s[i] == "E" and s[i - 1] == "E":
        ans[i] = ans[i - 1] - 1
    elif (s[i] == "E" and s[i - 1] == "W") or (s[i - 1] == "E" and s[i] == "W"):
        ans[i] = ans[i - 1]
    else:
        ans[i] = ans[i - 1] + 1
print(min(ans))
