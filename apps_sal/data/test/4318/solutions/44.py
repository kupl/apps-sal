n = int(input())
a = list(map(int, input().split()))
s, t = 0, 0
for i in a:
    if i >= s:
        s = i
        t += 1
print(t)
