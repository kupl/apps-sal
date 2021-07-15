x, y = tuple(map(int, input().split(' ')))
n = int(input()) - 1
a = (x, y, y - x, -x, -y, -y + x)
#print(a)

print(a[n%6]%1000000007)
