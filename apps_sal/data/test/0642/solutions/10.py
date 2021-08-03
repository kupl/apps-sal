n, m = list(map(int, input().split()))

if m > 0:
    num = [int(x) for x in input().split()]
    num.sort()

ret = True

if m > 0:
    if num[0] == 1 or num[m - 1] == n:
        ret = False

if m > 2:
    for i in range(m - 2):
        if num[i] + 2 == num[i + 1] + 1 == num[i + 2]:
            ret = False

print("YES" if ret else "NO")
