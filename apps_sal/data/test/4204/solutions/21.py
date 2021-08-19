s = input()
s = str(s)
k = int(input())
n = len(s)
for i in range(n):
    if s[i] != '1':
        break
if k <= i:
    print(1)
else:
    print(s[i])
