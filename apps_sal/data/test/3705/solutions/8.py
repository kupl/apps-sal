n = int(input())
s = input()
c = 0
for i in s:
    if i == '8':
        c += 1
cc = n // 11
print(min(cc, c))
