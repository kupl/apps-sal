def f(n, a):
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else :
                return count
        count += 1

n = int(input())
a = [int(s) for s in input().split()]
print(f(n,a))
