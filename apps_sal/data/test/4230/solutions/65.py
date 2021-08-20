(s, n) = input().split(' ')
min = 100
if int(n) != 0:
    num = input().split(' ')
else:
    num = []
for i in range(-102, 102):
    if str(i) not in num:
        cal = abs(int(s) - int(i))
    if min > cal:
        min = cal
        ans = int(i)
print(ans)
