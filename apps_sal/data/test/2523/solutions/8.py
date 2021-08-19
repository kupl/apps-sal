S = input()
l = len(S)
ans = l
'\nif len(set(list(S))) == 1 and S[0] == "0":\n    print(0)\n    return\n'
for i in range(l - 1):
    if S[i] != S[i + 1]:
        ans = min(ans, max(l - i - 1, i + 1))
print(ans)
