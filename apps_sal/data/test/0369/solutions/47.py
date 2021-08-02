N, M = list(map(int, input().split()))
S = input()
S = S[::-1]
l = len(S)

idx = 0
answer = []
flag = False
while True:
    if l - idx > M:
        m = M
    else:
        m = l - idx - 1
        flag = True
    if S[idx + m] == '0':
        answer.append(m)
        idx += m
        if flag:
            break
    else:
        while S[idx + m] == '1':
            m -= 1
            if m == 0:
                print((-1))
                return
        answer.append(m)
        idx += m

if answer[-1] == 0:
    answer.pop()
answer = answer[::-1]
print((' '.join(map(str, answer))))
