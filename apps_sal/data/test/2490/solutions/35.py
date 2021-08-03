N = [0] + list(map(int, list(input())))
L = len(N)
ans = 0
for i in range(L - 1, -1, -1):
    if N[i] == 10:
        if i == 0:
            ans += 1
        else:
            N[i - 1] += 1
            N[i] = 0
    if N[i] < 5:
        ans += N[i]
    elif N[i] > 5:
        ans += 10 - N[i]
        N[i - 1] += 1
    else:
        if i == 0:
            ans += N[i]
        else:
            if N[i - 1] >= 5:
                N[i - 1] += 1
                ans += 5
            else:
                ans += N[i]

print(ans)
