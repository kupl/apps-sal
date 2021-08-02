n = int(input())
s = list(map(int, input().split()))
q = set()
p = []
m = min(s)
z = 0
for i in range(len(s)):
    if s[i] == m:
        p.append(i)
z = [p[i + 1] - p[i] for i in range(len(p) - 1)]
print(min(z))
