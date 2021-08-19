N = int(input())
s1 = list(input())
s2 = list(input())

s = list(zip(s1, s2))
ss = []

skip = 0
for i in s:
    if skip:
        skip = 0
        continue

    if i[0] != i[1]:
        skip = 1
    ss.append(i)
# print(ss)


mod = 10**9 + 7
ans = 1
if ss[0][0] == ss[0][1]:
    f = 1
    ans *= 3
else:
    f = 0
    ans *= 6

# f = 1 : X
for i in range(1, len(ss)):
    if ss[i][0] == ss[i][1]:
        nf = 1
    else:
        nf = 0

    if f:
        ans *= 2
    else:
        if not nf:
            ans *= 3
    ans %= mod
    f = nf
print(ans)
