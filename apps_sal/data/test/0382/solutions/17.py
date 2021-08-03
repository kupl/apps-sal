def coun(s, t):
    d = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            d += 1
    return(d)


n, m, q = list(map(int, input().split()))
s = input()
t = input()
x = [0]

for j in range(n):
    x.append(coun(s[:j + 1], t))
for i in range(q):
    l, r = list(map(int, input().split()))
    r += 1
    if m <= r - l:
        print(x[r - 1] - x[max(0, l + m - 2)])
    else:
        print(0)
