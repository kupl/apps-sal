import sys
inp = sys.stdin
y = int(inp.readline()) + 1


def check_dif(num):
    s = str(num)
    ok = 1
    for i in range(len(s)):
        if s[i] in s[i + 1:]:
            ok = 0
    return ok


while check_dif(y) == 0:
    y += 1
print(y)
