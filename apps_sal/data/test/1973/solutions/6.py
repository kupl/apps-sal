n = int(input())
a = list(map(int, input().split()))
c = [0] * 11
ma = 1
for i in range(n):
    c[a[i]] += 1
    for k in range(1, 11):
        if c[k] > 0:
            c[k] -= 1
            s = {}
            for j in range(1, 11):
                if c[j] > 0:
                    if c[j] not in s:
                        s[c[j]] = 1
                    else:
                        s[c[j]] += 1
            c[k] += 1
            if len(s) == 1:
                ma = max(ma, i + 1)
                break

print(ma)

