n, m = list(map(int, input().split()))
groups = list(map(int, input().split()))
temp = m
buses = 1
for i in groups:
    if(i <= temp):
        temp -= i
    else:
        temp = m - i
        buses += 1
print(buses)
