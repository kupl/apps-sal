n = int(input())
p = list('zabcdefghijklmnopqrstuvwxy')
num = ''
while n > 26:
    a = p[n % 26]
    num += a
    if n % 26 == 0:
        n = n // 26 - 1
    else:
        n = n // 26
num += p[n % 26]
new_num = num[::-1]
print(new_num)
