s = input()
a = "10" * 10**5
b = "01" * 10**5
aa, bb = 0, 0
for i in range(len(s)):
    if s[i] == a[i]:
        bb += 1
    else:
        aa += 1
print(min(aa, bb))
