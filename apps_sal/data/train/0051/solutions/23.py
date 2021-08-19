import sys
lines = sys.stdin.readlines()
'\n(n, p) = map(int, lines[0].strip().split(" "))\nranges = []\nfor i in range(1, n+1):\n    (l, r) = map(int, lines[i].strip().split(" "))\n    ranges.append((l,r))\n\nprobs = []\nfor lr in ranges:\n    poss = lr[1]//p - (lr[0]-1)//p\n    probs.append(poss/(lr[1]-lr[0]+1))\n\nres = 0\nfor i in range(n):\n    res += probs[i] + probs[i-1] - probs[i] * probs[i-1]\nprint(res * 2000)\n'
N = int(lines[0].strip())
for i in range(1, 1 + N):
    (n, k, d1, d2) = map(int, lines[i].strip().split(' '))
    if n % 3 != 0:
        print('no')
        continue

    def solve(da, db):
        tmp = k - da - db
        if tmp % 3 != 0:
            return True
        b = tmp // 3
        a = b + da
        c = b + db
        if min(a, b, c) < 0:
            return True
        if n // 3 >= max(a, b, c):
            return False
        else:
            return True
    cannot = True
    if cannot:
        cannot = solve(d1, d2)
    if cannot:
        cannot = solve(d1, -d2)
    if cannot:
        cannot = solve(-d1, d2)
    if cannot:
        cannot = solve(-d1, -d2)
    if cannot:
        print('no')
    else:
        print('yes')
