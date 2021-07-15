n = int(input())
x = list(map(int,input().split()))

x_sort = sorted(x)
lenth = len(x)
low = x_sort[int(lenth/2)-1]
high = x_sort[int(lenth/2)]

for y in x:
    if y <= low:
        print(high)
    else:
        print(low)
