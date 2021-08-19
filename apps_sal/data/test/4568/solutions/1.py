N = int(input())
S = input()
ans = 0
for i in range(1, N - 1):
    set1 = set(S[:i])
    set2 = set(S[i:])
    z = set1.intersection(set2)
    ans = max(ans, len(z))
print(ans)
