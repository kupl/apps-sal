n = int(input())
a = list(map(int, input().split()))
s = 0
for x in a:
    k = 0
    while x % 2 == 0:
        k += 1
        x //= 2
    s += k
print(s)
