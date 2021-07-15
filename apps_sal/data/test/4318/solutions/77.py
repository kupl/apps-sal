n = int(input())
h = list(map(int, input().split()))
a = h[0]
b = 0
for i in h:
    if i >= a:
        a = i
        b += 1
print(b)
