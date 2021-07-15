price = int(input())

for n in range (1,10000):
    payment = n*1000
    if payment>=price:
        print(payment-price)
        return
