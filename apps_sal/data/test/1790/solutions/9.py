n = int(input())
myset = set()
for i in range(n):
    s = list(map(int, input().split()))
    r, s = s[0], s[1:]
    if i == 0:
        myset = set(s)
    else:
        myset &= set(s)
print(' '.join(map(str, myset)))
