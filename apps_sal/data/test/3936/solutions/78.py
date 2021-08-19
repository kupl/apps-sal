n = int(input())
s1 = input()
s2 = input()
MOD = 10 ** 9 + 7
for (i, (a, b)) in enumerate(zip(s1, s2)):
    if i == 0:
        if a != b:
            dp = 6
        else:
            dp = 3
        prev = (a, b)
    elif prev[0] == a and prev[1] == b:
        continue
    elif a == b:
        if prev[0] == prev[1]:
            dp *= 2
            dp %= MOD
            prev = (a, b)
        else:
            prev = (a, b)
    elif prev[0] == prev[1]:
        dp *= 2
        dp %= MOD
        prev = (a, b)
    else:
        dp *= 3
        dp %= MOD
        prev = (a, b)
print(dp)
