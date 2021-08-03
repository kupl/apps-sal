s = input()
withb = 0
withoutb = 0
ans = 0
for i in s:
    if i == "a":
        ans += withb + 1
        ans %= 10 ** 9 + 7
        withoutb += withb + 1
        withoutb %= 10 ** 9 + 7
    elif i == "b":
        withb += withoutb
        withb %= 10 ** 9 + 7
        withoutb = 0
print(ans % (10 ** 9 + 7))
