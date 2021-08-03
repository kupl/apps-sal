s1 = input()
s2 = input()

i1 = len(s1) - 1
i2 = len(s2) - 1
flag = True

ans = i1 + i2 + 2

while flag and i1 >= 0 and i2 >= 0:
    if s1[i1] == s2[i2]:
        ans -= 2
        i1 -= 1
        i2 -= 1
    else:
        flag = False

print(ans)
