n = int(input())
s = input()
idx, cur = 0, 1
d = ''
while idx < n:
    d += s[idx]
    idx += cur
    cur += 1
print(d)
