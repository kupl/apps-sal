s=0
cur = 0
x = int(input())
y = list(map(int, input().split(' ')))

for i in y:
    off = i + cur
    add = -off
    s += abs(add)
    cur += add

print(s)

