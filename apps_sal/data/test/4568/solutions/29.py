N = int(input())
S = input()

cnt = []
for n in range(1, N):
    x = sorted(S[:n])
    y = sorted(S[n:])
    cnt.append(len(set(x) & set(y)))

print(max(cnt))
