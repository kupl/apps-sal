S = input() + "R"
R = 0
L = 0
ans = [0] * (len(S) - 1)
for i in range(len(S) - 1):
    if S[i] == "R":
        if S[i + 1] == "L":
            R += 1
            if R % 2 == 0:
                ans[i] += R // 2
                ans[i + 1] += R // 2
            else:
                R -= 1
                ans[i] += R // 2 + 1
                ans[i + 1] += R // 2
            point = i
        else:
            R += 1
    else:
        if S[i + 1] == "R":
            L += 1
            if L % 2 == 0:
                ans[point] += L // 2
                ans[point + 1] += L // 2
            else:
                L -= 1
                ans[point] += L // 2
                ans[point + 1] += L // 2 + 1
            R = 0
            L = 0
        else:
            L += 1

print((' '.join(map(str, ans))))
