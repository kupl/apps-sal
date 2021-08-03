n = int(input())
l = list(map(int, input().split()))
a = l.count(1)
b = l.count(2)
if a == b:
    print(a)
elif a < b:
    print(a)
elif a > b:
    print(b + (a - b) // 3)
