def mp():
    return map(int, input().split())

n = int(input())
a = list(mp())

l = a.count(0)
r = a.count(1)

for i in range(n):
    if a[i] == 0:
        l -= 1
    else:
        r -= 1
    if l == 0 or r == 0:
        print(i + 1)
        break
