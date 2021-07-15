n = int(input())
s = input()
inv = {'L': 'R', 'R': 'L', 'D': 'U', 'U': 'D'}

res = 1

i = 0

t = set()
while i < len(s):
    d = s[i]
    if inv[d] in t:
        res += 1
        t = set()
    t.add(d)
    i += 1

print(res)

