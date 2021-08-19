input()
s = input()
not8 = [i for i, c in enumerate(s) if c != '8']
is8 = [i for i, c in enumerate(s) if c == '8']

n = len(s)
moves = (n - 11) // 2

if moves >= len(not8):
    print('YES')
    raise SystemExit(0)
if moves >= len(is8):
    print('NO')
    raise SystemExit(0)

not8 = not8[moves:]
is8 = is8[moves:]

# print(not8, is8)

if is8[0] < not8[0]:
    print('YES')
    raise SystemExit(0)
else:
    print('NO')
    raise SystemExit(0)
