n = int(input())
a = list(map(int, input().split()))

for i in range(100):
    for j in range(len(a)):
        if a[j]%2 == 0:
            a[j] //= 2
        else:
            print(i)
            return

