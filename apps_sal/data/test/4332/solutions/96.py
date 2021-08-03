n = int(input())
str_n = str(n)
sum_n = 0
for i in range(len(str_n)):
    sum_n += int(str_n[i])

if n % sum_n == 0:
    print('Yes')
else:
    print('No')
