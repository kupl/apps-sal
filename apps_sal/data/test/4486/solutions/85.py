s = str(input())
k = 0
odd = ''
for k in range(len(s)):
    if k % 2 == 0:
        odd += s[k]
print(odd)
