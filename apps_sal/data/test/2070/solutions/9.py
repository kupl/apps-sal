w = [int(x) for x in input().split()]
c = [{} for i in range(26)]
(val, s) = (0, 0)
for i in [ord(ch) - ord('a') for ch in input()]:
    if s - w[i] in c[i]:
        val += c[i][s - w[i]]
    c[i][s] = c[i][s] + 1 if s in c[i] else 1
    s += w[i]
print(val)
