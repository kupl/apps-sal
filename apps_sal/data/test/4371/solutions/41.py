S = input()
N = 1000

for i in range(len(S) - 2):
    N = min(N, abs(753 - int(S[i : i + 3])))
print(N)
