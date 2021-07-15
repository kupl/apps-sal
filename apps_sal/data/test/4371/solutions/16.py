S = input()

ans = 753
for i in range(len(S) - 2):
    x = int(S[i:i + 3])
    dif = abs(x - 753)
    ans = min(ans, dif)

print(ans)
