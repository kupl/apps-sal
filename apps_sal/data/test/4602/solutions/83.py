n = int(input())
k = int(input())
x = list(map(int, input().split()))
a = 0
for i in x:
    if 2 * i < 2 * (k - i):
        a += 2 * i
    else:
        a += 2 * (k - i)
print(a)
