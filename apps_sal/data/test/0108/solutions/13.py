s = list(input())
want = "abcdefghijklmnopqrstuvwxyz"

j = 0
for i in range(len(s)):

    if j >= 26:
        break

    if s[i] <= want[j]:
        s[i] = want[j]
        j += 1


if j < 26:
    print(-1)
else:
    ans = "".join(s)
    print(ans)
