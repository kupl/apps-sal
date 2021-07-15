s = input()
n = int(s[:-1])
s = s[-1]
n -= 1
ans = (16) * (n // 4) 
n %= 4
if n == 0:
    ans += 0
if n == 1:
    ans += 7
if n == 2:
    ans += 0
if n == 3:
    ans += 7
#print(ans)
if s in 'f':
    ans += 1
if s in 'e':
    ans += 2
if s in 'd':
    ans += 3
if s in 'a':
    ans += 4
if s in 'b':
    ans += 5
if s in 'c':
    ans += 6

print(ans)

