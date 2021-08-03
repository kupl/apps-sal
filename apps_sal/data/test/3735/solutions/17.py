n = int(input())
s = 0
m = 0
while(m <= n):
    s = s + 9
    m = m * 10 + 9
y1 = n - (m // 10)
s = s - 9
y = str(y1)
for i in y:
    s = s + int(i)
print(s)
