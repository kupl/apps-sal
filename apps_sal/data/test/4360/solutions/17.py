n = int(input())
a = list(map(int, input().split()))
s = 0
for i in a:
    s += 1 / i
print(1 / s)
