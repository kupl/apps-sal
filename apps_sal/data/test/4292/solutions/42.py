N,K = map(int,input().split())
fruit = [int(i) for i in input().split()]

fruit.sort()
price = 0
for i in range(N) :
    if i>K-1 :
        break
    price += fruit[i]
    
print(price)
