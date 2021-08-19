(n, k) = list(map(int, input().split()))
s = input()
max1 = 0
min1 = 100000
for i in s:
    max1 = max(max1, ord(i))
    min1 = min(min1, ord(i))
aim = 0
if k <= n:
    for i in range(min(n, k) - 1, -1, -1):
        if ord(s[i]) < max1:
            aim = i
            break
    min2 = max1
    for i in s:
        if ord(s[aim]) < ord(i) and min2 > ord(i):
            min2 = ord(i)
    fin = s[:aim] + chr(min2) + chr(min1) * (k - aim - 1)
    print(fin)
else:
    print(s + chr(min1) * (k - n))
