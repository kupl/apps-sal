3

b, k = list(map(int, input().split()))
a = list(map(int, input().split()))

cur = 0
for c in a:
    cur = (cur * b + c) % 2

if cur == 0:
    print("even")
else:
    print("odd")
