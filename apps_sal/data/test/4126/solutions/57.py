S = input()
ans = "No"
if S == S[::-1] and \
    S[:int((len(S) - 1) / 2)] == S[:int((len(S) - 1) / 2)][::-1] and \
    S[int((len(S) + 3) / 2) - 1:] == S[int((len(S) + 3) / 2) - 1:][::-1]: ans = "Yes"
print(ans)
