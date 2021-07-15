import sys

def input():
    return sys.stdin.readline()

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prices_n_sales = sorted(list(zip(b,(i-j for i,j in zip(a,b)))), key = lambda x:x[1])
# купить не менее k товаров
total = sum(ps[0] + ps[1] for ps in prices_n_sales[:k])
i = k
if i == n:
    print(total)
    return
while prices_n_sales[i][1] < 0:
    total += prices_n_sales[i][0] + prices_n_sales[i][1]
    i += 1
    if i >= n: break
print(total + sum(ps[0] for ps in prices_n_sales[i:]))


