n = int(input())
arr = map(int, input().split())
sm = sum(arr)
f = -1
h = 0
k = int(input())
for i in range(k):
    (a, b) = map(int, input().split())
    if a <= sm <= b:
        f = sm
        h = 1
    elif a > sm and (not h):
        f = a
        h = 1
print(f)
