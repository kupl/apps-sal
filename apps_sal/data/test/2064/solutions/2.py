n = int(input())
if n % 2 == 1:
    s = '7'
    n = n - 3
else:
    s = '1'
    n = n - 2
while n > 0:
    s = s + '1'
    n = n - 2
print(s)
