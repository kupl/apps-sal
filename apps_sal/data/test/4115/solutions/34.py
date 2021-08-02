S = input()
listS = list(S)
cnt = 0
if len(S) % 2 == 0:
    for i in range(len(S) // 2):
        if S[i] != S[-(i + 1)]:
            cnt += 1
else:
    for i in range((len(S)) // 2):
        if S[i] != S[-(i + 1)]:
            cnt += 1

print(cnt)
