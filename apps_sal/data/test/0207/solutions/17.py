n = int(input())
a = list(map(int, input().split(' ')))

if (n & 1) and (a[0] & 1) and (a[-1] & 1):
    print("Yes")
else:
    print("No")
