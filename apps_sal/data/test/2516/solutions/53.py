n, p = map(int, input().split())
s = input()
r = set()
last = 0
d = {0: 0}
total = 0
rem = 0
if p == 2:
    for i in range(0, len(s)):
        if int(s[i]) % 2 == 0:
            total += i + 1
    print(total)
elif p == 5:
    for i in range(0, len(s)):
        if int(s[i]) % 5 == 0:
            total += i + 1
    print(total)



else:
    power = 1
    for i in range(len(s) - 1, -1, -1):  # handling of 0's as n and rem
        n = int(s[i]) * power + rem
        power *= 10
        power = power % p
        rem = n % p
        if rem in d.keys():
            d[rem] += 1
        else:
            d[rem] = 1
        total += d[rem] - 1
    print(total + d[0])
