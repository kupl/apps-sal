n = int(input())
s1 = input().rstrip()
s = (')'.join(s1.split('('))).split(')')
fl = 0
ans = 0
k = 0
for i in range(len(s)):
    if i % 2 == 0:
        for j in s[i].split('_'):
            if len(j) > ans:
                ans = len(j)
    else:
        for j in s[i].split('_'):
            if len(j) > 0:
                k += 1
print(ans, k)
