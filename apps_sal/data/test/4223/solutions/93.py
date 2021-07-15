N = int(input())
S = input()

res = ""
pre = ""
for s in S:
    if pre != s:
        res += s
    pre = s

print((len(res)))

