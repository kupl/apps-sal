S = input()
cnt = 0
if S[0] == 'R':
    cnt += 1
    if S[1] == 'R':
        cnt += 1
        if S[2] == 'R':
            cnt += 1
        else:
            pass
elif S[1] == 'R':
    cnt += 1
    if S[2] == 'R':
        cnt += 1
    else:
        pass
elif S[2] == 'R':
    cnt += 1
print(cnt)
