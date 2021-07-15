S = input()
N = len(S)
divs = [0]
for i in range(N - 1):
    if S[i] == "L" and S[i + 1] == "R":
        divs.append(i + 1)
divs.append(N)
ans = [0] * N
for start, end in zip(divs, divs[1:]):
    sub = S[start:end]
    M = end - start
    for j in range(M - 1):
        if sub[j] == "R" and sub[j + 1] == "L":
            if j % 2:
                ans[start + j] = M // 2
            else:
                ans[start + j] = (M + 1) // 2
            ans[start + j + 1] = M - ans[start + j]
print((" ".join(map(str, ans))))

