S = input()
N = len(S)
num = 753
res = 10 ** 10
for i in range(N - 2):
    res = min(res, abs(int(S[i:i + 3]) - num))
print(res)
