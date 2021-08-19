eat = int(input())
pay = 0
discount = 0
count = 0
for i in range(eat):
    pay += 800
    count += 1
    if count % 15 == 0:
        discount += 200
print(pay - discount)
