S = list(input())
S.pop(-1)
if len(S) % 2 == 1:
    S.pop(-1)
while True:
    count = 0
    for i in range(int(len(S) / 2)):
        if S[i] == S[int(len(S) / 2) + i]:
            count += 1
            continue
        else:
            break
    if count == len(S) / 2:
        print(len(S))
        break
    S.pop(-1)
    S.pop(-1)
