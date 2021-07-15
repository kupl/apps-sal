s = input()
maxlen = 0
for i in range(len(s)):
    for j in range(1,len(s)+1):
        t = s[i:j]
        if all([c in 'ACGT' for c in s[i:j]]):
            maxlen = max(maxlen, j-i)
print(maxlen)
