S = input()
ans = [0] * len(S)
lr = 'r'
for i in range(len(S)):
    if (i == 0 or lr == 'l') and S[i] == 'R':
        c = 0
        lr = 'r'
        while S[i + c] == 'R':
            c += 1
        ans[i + c] += c // 2
        ans[i + c - 1] += (c + 1) // 2
    elif lr == 'r' and S[i] == 'L':
        c = 0
        lr = 'l'
        while i + c < len(S) and S[i + c] == 'L':
            c += 1
        ans[i] += (c + 1) // 2
        ans[i - 1] += c // 2
print(*ans)
