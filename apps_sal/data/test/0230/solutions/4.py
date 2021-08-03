n = int(input())
s = input()
ret = 0
for l in range(n):
    while s[l:l + ret + 1] in s[l + ret + 1:]:
        ret += 1
print(ret)
