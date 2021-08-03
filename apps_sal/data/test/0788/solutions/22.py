S = input()[1:]
ans = 1
for i in range(len(S)):
    if S[i] == '1':
        ans += 10
    else:
        ans += ord(S[i]) - ord('0')
print(ans)
