n = int(input())
a = list(map(int, input().split()))
b=[i for i in a if i > 0]
c=[i for i in a if i <= 0]
sb = 0
sc = 0
if len(b) > 0:
    sb = sum(b)
if len(c) > 0:
    sc = sum(c)
print(sb-sc)

