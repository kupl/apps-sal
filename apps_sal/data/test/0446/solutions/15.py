n = int(input())
l = []
k = 1
num = 0
while num <= 100000:
    num = ((2**k) - 1) * (2**(k - 1))
    if num <= 100000:
        l.append(num)
    k += 1
ans = 1
for each in l:
    if n % each == 0:
        ans = each
print(ans)
