s = input()
n, s = int(s[:-1]) - 1, ord(s[-1]) - ord('a')

blocks = n // 4
n = n % 4
offs = (n % 2)

locOffs = [4, 5, 6, 3, 2, 1][s]

ans = blocks * 16 + offs * 7 + locOffs
print(ans)
