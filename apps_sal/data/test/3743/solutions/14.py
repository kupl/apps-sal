

n = int(input())

check = 0

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        check = 1
        while n % i == 0:
            n /= i
        if n == 1:
            print(i)
            break
        else:
            print(1)
            break

if check == 0:
    print(n)
