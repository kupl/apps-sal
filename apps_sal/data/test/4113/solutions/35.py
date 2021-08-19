n = int(input())
res = 'No'
if n % 4 == 0:
    res = 'Yes'
while n > 0:
    if n % 7 == 0:
        res = 'Yes'
        break
    n -= 4
print(res)
