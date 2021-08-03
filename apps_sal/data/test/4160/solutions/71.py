x = int(input())
price = 100
answer = 0

while x > price:
    price = price + price // 100
    answer += 1

print(answer)
