s = input()
n = 0
t = 'a'
for i in s:
    n += min(abs(ord(i) - ord(t)), abs(26 - abs(ord(i) - ord(t))))
    t = i
print(n)
