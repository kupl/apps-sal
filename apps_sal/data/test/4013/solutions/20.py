n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse = True)
print(min(a[0] - a[-2], a[1] - a[-1]))
