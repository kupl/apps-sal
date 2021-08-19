x = input().strip()
n = int(x[:len(x) - 1])
c = x[len(x) - 1]
# print(n);
# print(c);
ans = 0
ans += ((n - 1) // 4) * 16
n %= 4

colVal = 0
if(c == 'a'):
    colVal = 4
if(c == 'b'):
    colVal = 5
if(c == 'c'):
    colVal = 6
if(c == 'd'):
    colVal = 3
if(c == 'e'):
    colVal = 2
if(c == 'f'):
    colVal = 1

if n == 1 or n == 3:
    ans += colVal
if n == 2 or n == 0:
    ans += 7
    ans += colVal
print(ans)
