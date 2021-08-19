S = input()
check = []
flg = 0
ans = []
for i in range(len(S)):
    check.append(S[i])
    if S[i] == 'L':
        flg = 1
    if S[i] == 'R' and flg == 1:
        check.pop()
        for j in range(len(check)):
            if check[j] == 'L':
                o = j
                break
        answer = [0 for p in range(len(check))]
        if len(check) % 2 == 0:
            answer[o] = int(len(check) / 2)
            answer[o - 1] = int(len(check) / 2)
        elif o % 2 == 0:
            answer[o] = len(check) // 2 + 1
            answer[o - 1] = len(check) // 2
        else:
            answer[o] = len(check) // 2
            answer[o - 1] = len(check) // 2 + 1
        for z in answer:
            ans.append(z)
        check = ['R']
        flg = 0
for j in range(len(check)):
    if check[j] == 'L':
        o = j
        break
answer = [0 for p in range(len(check))]
if len(check) % 2 == 0:
    answer[o] = int(len(check) / 2)
    answer[o - 1] = int(len(check) / 2)
elif o % 2 == 0:
    answer[o] = len(check) // 2 + 1
    answer[o - 1] = len(check) // 2
else:
    answer[o] = len(check) // 2
    answer[o - 1] = len(check) // 2 + 1
for z in answer:
    ans.append(z)
for m in ans:
    print(m, end=' ')
print()
