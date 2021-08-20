n = int(input())
arr = list(map(int, input().strip().split(' ')))
a = arr.count(1)
b = arr.count(2)
if b >= a:
    print(a)
else:
    s = b
    s = s + (a - b) // 3
    print(s)
