n = int(input())
l = list(map(int, input().split()))
m = list(map(int, input().split()))
a = 0
b = 0

for j in range(n):
    b = sum(l[0:j + 1]) + sum(m[j:n + 1])
    if a < b:
        a = b
    else:
        pass

print(a)
