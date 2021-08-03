n = int(input())
s = input()
i = 0
while i < n and s[i] == '1':
    i += 1
if i < n:
    print(i + 1)
else:
    print(i)
