n = int(input())
socks = [int(x) for x in input().split()]

on = set()
m = 0
i = 0
for s in socks:
    if s in on:
        m = max(m, i)
        i -= 1
    else:
        on.add(s)
        i += 1
print(max(m, i))
    

