n = int(input())
s = [input() for i in range(n)]
s = [(x, x.count("s"), x.count("h")) for x in s]
s.sort(key=lambda x: x[2] / float(x[1] + 1e-6))
s = ''.join(x[0] for x in s)

pre, ans = 0, 0
for x in s:
    if (x == "s"):
        pre += 1
    else:
        ans += pre
print(ans)
