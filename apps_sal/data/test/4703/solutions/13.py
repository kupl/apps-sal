s = input()
n = len(s) - 1
res = 0
for i in range(1 << n):
    num_str = s[0]
    for j in range(n):
        if i >> j & 1 == 0:
            num_str += s[j + 1]
        else:
            res += int(num_str)
            num_str = s[j + 1]
    res += int(num_str)

print(res)
