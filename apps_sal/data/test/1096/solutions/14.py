s = input()

boundary = ['1', '8', 'a', 'h']

ans = 8 - 3 * (s[0] in boundary) - 3 * (s[1] in boundary) + (s[1] in boundary) * (s[0] in boundary)

print(ans)
