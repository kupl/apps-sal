S = input()
MIN = 10 ** 8
flag = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        flag = 0
        MIN = min(MIN, max(i + 1, len(S) - i - 1))
if flag:
    MIN = len(S)
print(MIN)
