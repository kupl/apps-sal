b = "aeiouy"
n = int(input())
s = input()
a = [0] * len(s)
for i in range(1, len(s)):
    if s[i - 1] in b and s[i] in b:
        a[i] = 1
for i in  range(len(s)):
    if not a[i]:
        print(s[i], end="")
        
