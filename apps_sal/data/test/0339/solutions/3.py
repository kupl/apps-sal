n = int(input())
k = int(input())
A = int(input())
B = int(input())
coins = 0
while (n != 1):
    if(n % k == 0 and ((n - n / k) * A) > B):
        coins += B
        n /= k
    elif (n % k == 0):
        coins += A * (n - 1)
        n = 1
    else:
        coins += A * (n % k)
        n = n - (n % k)
print(int(coins))
