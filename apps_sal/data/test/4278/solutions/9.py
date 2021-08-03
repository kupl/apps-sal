from math import factorial as f

n = int(input())
d = {}

for _ in range(n):
    s = list(input())
    s.sort()
    s = "".join(s)

    is_ok = d.get(s, False)
    if is_ok:
        d[s] += 1
    else:
        d[s] = 1

ans = 0

for i in d.values():
    if i >= 2:
        ans += f(i) // f(i - 2) // f(2)

print(ans)
