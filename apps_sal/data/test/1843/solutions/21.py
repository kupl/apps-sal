t = int(input())
for _ in range(t):
    inp = int(input())
    print(inp * (inp + 1) // 2 - 2 * (2 ** (len(bin(inp)) - 2) - 1))
