n = int(input())
a = list(map(int, input().split()))
a.sort()
num = a[0]

for i in a:
    num = (num + i) / 2
print(num)
