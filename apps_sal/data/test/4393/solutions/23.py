n = int(input())
s = input()
d = ""
l = 0
for i in range(n):
    d = d + s[l]
    l = l + i + 1
    if l >= n:
        break

print(d)
