N = int(input())
S = input()

cnt = 0
for i in range(N):
    s1 = set(S[:i])
    s2 = set(S[i:])
    l: int = len(s1 & s2)
    if l > cnt:
        cnt = l

print(cnt)
