cur = '1'
beautiful = [int(cur, 2),]
while int(cur, 2) < 1e5:
    cur = '1' + cur + '0'
    beautiful.append(int(cur, 2))
# print(beautiful)
n = int(input())
for x in beautiful[::-1]:
    if n % x == 0:
        print(x)
        break


