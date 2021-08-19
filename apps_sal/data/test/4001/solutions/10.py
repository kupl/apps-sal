n = int(input())
a = list(map(int, input().split()))
a.sort()
x = a[-1]
while a:
    d = a.pop()
    if x % d != 0 or (a and a[-1] == d):
        y = d
        break
print(x, y)
