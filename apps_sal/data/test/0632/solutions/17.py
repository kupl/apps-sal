t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    for i in range(2, n + 1):
        if n % i == 0:
            break
    n += i
    k -= 1
    print(n + 2 * k)
