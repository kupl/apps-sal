s = input()
table = [0] * 30
def o(x): return ord(x) - ord('a')


kind = 0
for c in s:
    if table[o(c)] == 0:
        kind += 1
    table[o(c)] += 1

if kind > 2 and s[0] != s[-1]:
    print("First") if len(s) % 2 == 1 else print("Second")
elif kind > 2 and s[0] == s[-1]:
    print("Second") if len(s) % 2 == 1 else print("First")
else:
    print("Second")
