S = input()
a = len(S)
print(sum(S[i] != S[a - i - 1]for i in range(a // 2)))
