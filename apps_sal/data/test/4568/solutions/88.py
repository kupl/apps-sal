N = int(input())
S = input()
r = 0
for i in range(1, N):
    s1 = S[:i]
    s2 = S[i:]
    r = max(len(set(s1) & set(s2)), r)
print(r)
