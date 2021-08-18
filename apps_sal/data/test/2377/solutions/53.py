n, H = list(map(int, input().split()))
a = []
b = []
for i in range(n):
    ai, bi = list(map(int, input().split()))
    a.append(ai)
    b.append(bi)

ans = 0
amax = max(a)
b.sort(reverse=True)
i = 0
while H > 0:
    if i < n:
        if amax < b[i]:
            H -= b[i]
            ans += 1
            i += 1
        else:
            ans += H // amax
            if H % amax != 0:
                ans += 1
            break
    else:
        ans += H // amax
        if H % amax != 0:
            ans += 1
        break

print(ans)
