n, b, a = [int(item) for item in input().split()]
s = [int(item) for item in input().split()]

max_a = a
ans = 0

rem = [0] * n
rem[-1] = s[-1]
for i in range(n - 2, -1, -1):
    rem[i] = rem[i + 1] + s[i]

for i, sun in enumerate(s):
    # print(b, a, sun)
    if b == 0 and a == 0:
        break
    if b == 0:
        a -= 1
    elif a == 0:
        b -= 1
        if sun and a < max_a:
            a += 1
    else:
        if a == max_a:
            a -= 1
        else:
            if sun:
                a += 1
                b -= 1
            else:
                if max_a - a < rem[i]:
                    a -= 1
                else:
                    b -= 1

    ans += 1

print(ans)

