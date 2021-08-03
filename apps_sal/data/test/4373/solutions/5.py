n = int(input())
a = list(map(int, input().split()))
sa = sorted(a)
ptr = 0
for i in range(1, n + 2):
    while ptr < n and sa[ptr] < i:
        ptr += 1
    if ptr == n:
        print(i - 1)
        break
    ptr += 1
