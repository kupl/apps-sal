n, m = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
l1 = [0 for i in range(101)]
for i in l:
    l1[i] = l1[i] + 1
for i in range(100, 0, -1):
    r = 0
    for j in range(1, 101):
        r = r + l1[j] // i
    if (r >= n):
        print(i)
        return
print(0)
