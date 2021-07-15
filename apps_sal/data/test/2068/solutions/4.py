n = int(input())
d = {'polycarp': 1}
m = 1
for i in range(n):
    s = input().lower().split()
    d[s[0]] = d[s[2]] + 1
    if d[s[0]] > m:
        m = d[s[0]]
print(m)
