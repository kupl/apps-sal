a = int(input())
s = bin(a)
k = 0
for i in range(len(s)):
    if (s[i] == '1'):
        k += 1
print(k)
