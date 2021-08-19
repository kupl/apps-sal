next = {}
appear = {}
front = {}
n = int(input())
for i in range(1, n + 1):
    [a, b] = [int(x) for x in input().split()]
    next[a] = b
    front[a] = True
    front[b] = False
    if a not in appear:
        appear[a] = 1
    else:
        appear[a] = 2
    if b not in appear:
        appear[b] = 1
    else:
        appear[b] = 2
a = 0
b = 0
for x in appear.keys():
    if appear[x] == 1 and front[x]:
        print(x, next[0], end=' ')
        a = x
        b = next[0]
cnt = 2
for i in range(0, n - 1):
    if cnt == n:
        break
    print(next[a], end=' ')
    cnt += 1
    if cnt == n:
        break
    print(next[b], end=' ')
    cnt += 1
    if cnt == n:
        break
    a = next[a]
    b = next[b]
print()
