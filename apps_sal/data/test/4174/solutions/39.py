(n, x) = map(int, input().split())
l = list(map(int, input().split()))
L = [0] + l
a = 0
count = 1
for i in l:
    a += i
    if a <= x:
        count += 1
print(count)
