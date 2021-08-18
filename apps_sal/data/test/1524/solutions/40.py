S = input()

ans = [1 for _ in range(len(S))]
count = 0
for i in range(len(S) - 1):
    if S[i] == 'R' and S[i + 1] == 'R':
        count += 1
        ans[i] -= 1
    if S[i] == 'R' and S[i + 1] == 'L':
        ans[i] += count // 2
        ans[i + 1] += count // 2
        if count % 2 == 1:
            ans[i + 1] += 1
        count = 0

count = 0
for i in range(len(S) - 1):
    if S[-i - 1] == 'L' and S[-i - 2] == 'L':
        count += 1
        ans[-i - 1] -= 1
    if S[-i - 1] == 'L' and S[-i - 2] == 'R':
        ans[-i - 1] += count // 2
        ans[-i - 2] += count // 2
        if count % 2 == 1:
            ans[-i - 2] += 1
        count = 0

for i in range(len(S)):
    if i != len(S) - 1:
        print(ans[i], end=" ")
    else:
        print(ans[i])
