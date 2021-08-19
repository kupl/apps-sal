inp_s = input()
mod = 10 ** 9 + 7
i = 0
l = len(inp_s)
r = 0
while i < l:
    a = 0
    while i < l and inp_s[i] != 'b':
        if inp_s[i] == 'a':
            a += 1
        i += 1
    r = (r + r * a + a) % mod
    i += 1
print(r)
