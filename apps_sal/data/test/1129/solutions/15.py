n = int(input())
l = list(map(int, input().split()))
l.sort()
if n == 1:
    print(l[0])
elif n % 2 == 0:
    print(l[n // 2 - 1])
else:
    print(l[n // 2])
