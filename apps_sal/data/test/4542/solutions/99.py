S = input()
rest = S[0]
cnt = 0
for i in range(1, len(S)):
    if S[i] != rest:
        cnt += 1
        rest = S[i]
print(cnt)
