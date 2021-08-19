(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a_reverse = list(reversed(a))
b = sorted(a)
s = sum(a)
ans = []
for i in range(k + 1):
    if i > n:
        I = i - n
        for j in range(I):
            if j < n:
                ans1 = s - b[j]
        ans.append(ans1)
    elif i == n:
        ans.append(s)
    elif i == 0:
        ans.append(0)
    else:
        for h in range(i + 1):
            H = i - h
            c = []
            for x in range(h):
                c.append(a[x])
            for y in range(H):
                c.append(a_reverse[y])
            c.sort()
            S = sum(c)
            for g in range(1, k - i + 1):
                if g <= i:
                    if c[g - 1] < 0:
                        S -= c[g - 1]
            ans.append(S)
print(max(ans))
