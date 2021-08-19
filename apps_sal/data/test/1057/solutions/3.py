n = int(input())
s = input()
count_begin = 0
count_end = 0
i = 0
while s[i] == s[0]:
    count_begin += 1
    i += 1
i = -1
while s[i] == s[-1]:
    count_end += 1
    i -= 1
if s[0] == s[-1]:
    print((count_begin + 1) * (count_end + 1) % 998244353)
else:
    print((count_begin + count_end + 1) % 998244353)
