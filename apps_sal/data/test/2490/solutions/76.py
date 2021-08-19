N = [int(c) for c in input()][::-1]
N.append(0)
ans = 0
for i in range(len(N)):
    c = N[i]
    if c <= 4:
        ans += c
    elif 6 <= c:
        ans += 10 - c
        N[i + 1] += 1
    elif N[i + 1] < 5:
        ans += c
    else:
        ans += 10 - c
        N[i + 1] += 1
print(ans)
