n = int(input())

shop_row = [0] + list(map(int, input().split()))
house_row = list(map(int, input().split())) + [0]
perek = list(map(int, input().split()))

for i in range(len(house_row) - 2, -1, -1):
    house_row[i] += house_row[i + 1]
for i in range(1, len(shop_row)):
    shop_row[i] += shop_row[i - 1]
rez = [None] * n
for i in range(n):
    rez[i] = house_row[i] + shop_row[i] + perek[i]
rez.sort()

if len(rez) > 1:
    print(rez[0] + rez[1])
else:
    print(rez[0] + rez[0])




