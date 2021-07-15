n, m = list(map(int, input().split()))
s = input()
t = input()

ans = [i for i in range(1, n + 1)]
for i in range(m - n + 1):
    pos = []
    for j in range(n):
        if s[j] != t[i + j]:
            pos.append(j + 1)
    if len(pos) < len(ans):
        ans = pos

print(len(ans))
print(' '.join(map(str, ans)))

