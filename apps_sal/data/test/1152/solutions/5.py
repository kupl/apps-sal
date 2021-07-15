def get_inp(nf):
    a = b = 0
    for _ in range(nf):
        inp = input()
        a ^= int(inp.replace(' ', ''), 2)
        b = b * 2 + inp.count('1') % 2
    return a, b


n = int(input().split()[0])
if get_inp(n) == get_inp(n):
    print("Yes")
else:
    print("No")

