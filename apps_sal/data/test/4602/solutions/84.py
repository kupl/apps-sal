n = int(input())
k = int(input())
x = list(map(int, input().split()))
d = 0
for i in x:
    y = min(i, abs(k-i))
    d += 2*y
print(d)
