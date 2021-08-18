n = 0
k = 0
s = ""
for i in input().split():
    if n == 0:
        n = int(i)
    else:
        k = int(i)

s = str(input())
node = []
for i in range(len(s)):
    if s[int(i)] == '0':
        node.append(i + 1)

node.append(1000000000)


def check(dis):
    current = 0
    num = k - 2
    for i in range(len(node) - 1):
        if num < 1:
            break
        if node[i] - node[current] <= dis and node[i + 1] - node[current] > dis:
            current = i
            num -= 1
    if n - node[current] > dis:
        return -1

    return 1


left = 1
right = n
while left + 1 < right:
    mid = int((left + right) / 2)
    t = check(mid)
    if t == 1:
        right = mid
    else:
        left = mid
for i in range(left, right + 1):
    if check(i) == 1:
        print(i - 1)
        return
print(0)
