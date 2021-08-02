N = int(input())
S = input()

ans = 0
for i in range(N):
    s1, s2 = set(S[:i]), set(S[i:])
    tmp = len(s1.intersection(s2))
    if tmp > ans:
        ans = tmp


print(ans)
