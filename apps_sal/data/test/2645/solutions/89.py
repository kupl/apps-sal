g = 0
p = 0

ans = 0
for i in input():
    if i == "g":
        if p < g:
            ans += 1
            p += 1
        else:
            g += 1
    else:
        if p < g:
            p += 1
        else:
            g += 1
            ans -= 1

print(ans)
