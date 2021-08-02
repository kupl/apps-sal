r = 1
k = 0
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if (i % r == 0):
        k += 1
    while(i % (r * 2) == 0):
        r *= 2
        k = 1
print(r, k)
