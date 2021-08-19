N = int(input())
S = input()
copied = 1
for i in range(1, N // 2 + 1):
    # print(i, "\"{}\"".format(S[:i]), "\"{}\"".format(S[i:2*i]))
    if S[:i] == S[i:2 * i]:
        copied = i
print(N - copied + 1)
