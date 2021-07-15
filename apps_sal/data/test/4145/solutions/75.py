def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = int(input())
i = x-1
while True:
    i += 1
    if f(i):
        print(i)
        return
