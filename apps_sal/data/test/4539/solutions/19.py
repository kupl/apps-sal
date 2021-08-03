n = int(input())

nn = str(n)
ha_num = 0
for i in nn:
    ha_num += int(i)

if n % ha_num == 0:
    print('Yes')
else:
    print('No')
