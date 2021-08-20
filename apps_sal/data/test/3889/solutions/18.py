n = int(input())
s = input()
c = [0] * 26
for i in s:
    c[ord(i) - ord('a')] += 1
c.sort(reverse=1)
cur = 0
f = 1
for i in c:
    if i == 1:
        if cur <= 1:
            f = 0
            break
    cur += i
if n == 1:
    f = 1
print('Yes' if f else 'No')
