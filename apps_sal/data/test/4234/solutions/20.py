n = int(input())
s = input()
res = []
i = 0
ops = 0
while i < n:
    if i + 1 == n or s[i] == s[i + 1]:
        ops += 1
        i += 1
    else:
        res += [s[i], s[i + 1]]
        i += 2
print(ops)
print(''.join(res))
