MOD = 10 ** 9 + 7


n = int(input())
s = input()

cnt = s.count('?')
# print(cnt)

a, ab, abc = 0, 0, 0
a2, ab2, abc2 = 0, 0, 0
a3, ab3, abc3 = 0, 0, 0
a4, ab4, abc4 = 0, 0, 0
for i in s:
    if i == 'a':
        a += 1
    elif i == 'b':
        ab += a
        ab2 += a2
    elif i == 'c':
        abc += ab
        abc2 += ab2
        abc3 += ab3
    else:
        a2, ab2, abc2, ab3, abc3, abc4 = a2 + 1, ab2 + a, abc2 + ab, ab3 + a2, abc3 + ab2, abc4 + ab3
    # print(a, ab, abc)
    # print(a2, ab2, abc2)
    # print(a3, ab3, abc3)
    # print(a4, ab4, abc4)
    # print('=========')


if cnt == 0:
    pass
elif cnt == 1:
    abc *= 3
elif cnt == 2:
    abc *= 9
    abc2 *= 3
elif cnt == 3:
    abc *= 27
    abc2 *= 9
    abc3 *= 3
else:
    abc = (abc * (3 ** cnt) % MOD) % MOD
    abc2 = (abc2 * (3 ** (cnt - 1)) % MOD) % MOD
    abc3 = (abc3 * (3 ** (cnt - 2)) % MOD) % MOD
    abc4 = (abc4 * (3 ** (cnt - 3)) % MOD) % MOD

# print(abc, abc2, abc3, abc4)

ans = (abc + abc2 + abc3 + abc4) % MOD
print(ans)

