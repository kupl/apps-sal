N = int(input())
S = str(input())
ans = ''
for i in range(len(S)):
    if ord(S[i]) + N > 90:
        c = ord(S[i]) + N - 26
    else:
        c = ord(S[i]) + N
    ans += chr(c)
print(ans)
