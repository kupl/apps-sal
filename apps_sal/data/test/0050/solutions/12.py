def mp():
    return map(int, input().split())

n, m, r = mp()
s = list(mp())
b = list(mp())

t = r // min(s)
o = r % min(s)
p = max(b) * t

print(max(r, p + o))
