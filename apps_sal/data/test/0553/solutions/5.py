n = int(input())

s = [''] * (n)
for i in range(n):
    s[i] = input()

if (n == 1):
    print(6)
else:
    diff = 6

    for u in s:
        for v in s:
            kol = 0
            for i in range(6):
                if u[i] != v[i]:
                    kol += 1
            if kol > 0:
                diff = min(diff, kol)

    diff = max(0, diff - 1)
    print(diff // 2)
