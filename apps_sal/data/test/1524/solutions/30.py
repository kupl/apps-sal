S = input()
ans = [0] * len(S)
count = 0
for i in range(len(S)):
    if S[i] == 'R':
        count += 1
    else:
        if count % 2 == 0:
            ans[i - 1] += count // 2
            ans[i] += count // 2
        else:
            ans[i - 1] += count // 2 + 1
            ans[i] += count // 2
        count = 0
count = 0
for i in range(len(S) - 1, -1, -1):
    if S[i] == 'L':
        count += 1
    else:
        if count % 2 == 0:
            ans[i + 1] += count // 2
            ans[i] += count // 2
        else:
            ans[i + 1] += count // 2 + 1
            ans[i] += count // 2
        count = 0

for i in range(len(S)):
    ans[i] = str(ans[i])
print(' '.join(ans))
