n = int(input())
a = input().split()

if n % 2 == 1:
    print(" ".join((a[0::2][::-1] + a[1::2])))
else:
    print(" ".join((a[1::2][::-1] + a[0::2])))
