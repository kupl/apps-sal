n, d = map(int, input().split())
d -= 1
s, p, j = [*map(int, input().split())], [*map(int, input().split())], -1
for i in range(n):
    if s[d] + p[0] < s[i]:
        continue
    if i == d:
        s[i] += p[0]
        break
    else:
        s[i] += p[j]
        j -= 1
print(sorted(s, reverse=True).index(s[d]) + 1)
