n = int(input())
s = []

for i in range(n):
    sl = int(input())
    s.append(sl)

s.sort()
ans = sum(s)

i = 0
while ans > 0 and i < n:
    if ans % 10 != 0:
        print(ans)
        return
    else:
        if s[i] % 10 != 0:
            ans = ans - s[i]
        i += 1

print((ans % 10))
