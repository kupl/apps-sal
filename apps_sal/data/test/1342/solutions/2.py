# Returns the number of coins that is necessary for paying the amount
# with the two types of coins that have value of coin and coin + 1
def pay(coin, amount):
    if amount // coin < amount % coin:
        return -1;
    if amount < coin * (coin + 1):
        return amount // coin
    return (amount - 1) // (coin + 1) + 1;


def pay_all(coin):
    sum = 0
    for i in range(n):
        p = pay(coin, a[i])
        if p == -1:
            return -1
        sum += p
    return sum


n = int(input())
a = list(map(int, input().split()))
amin = min(a)
coin = amin
k = 1
p = -1
while p == -1:
    p = pay_all(coin)
    if p == -1 and amin % coin == 0:
        p = pay_all(coin - 1)
    k += 1
    coin = amin // k
print(p)
