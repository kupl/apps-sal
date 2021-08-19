N = int(input())
a = list(map(int, input().split()))
max_height = -1
s = 0
for i in a:
    max_height = max(max_height, i)
    d = max_height - i
    s += d
print(s)
