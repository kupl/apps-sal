n = int(input())
pre_res = 1
max_s = n * 9
s = input()
sums = [1] * (max_s + 1)
i = 1
while i <= max_s:
    sums[i] = i
    i += 1
for c in s:
    if c != '0':
        d = int(c)
        i = 1
        while i <= max_s:
            if sums[i] == i:
                sums[i] = d
            else:
                sums[i] += d
            i += 1
res = 1
i = 1
while i <= max_s:
    if sums[i] == i:
        res += 1
    i += 1
if res == 2:
    print('NO')
else:
    print('YES')
