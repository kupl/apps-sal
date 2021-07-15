N = int(input())
s = 1
t = 0
while N > 26**s + t:
    t += 26**s
    s += 1
N -= t
ans = []
for i in range(s):
    c = 0
    while N > 26**(s-i-1):
        N -= 26**(s-i-1)
        c += 1
    ans.append(chr(97+c))
print("".join(ans))
