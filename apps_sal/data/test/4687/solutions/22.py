from xml.dom import minidom


n, k = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort()

now = -1
idx = 0
while k > 0:
    if idx >= n:
        break
    a, b = AB[idx]
    k -= b
    now = a
    idx += 1
print(now)

