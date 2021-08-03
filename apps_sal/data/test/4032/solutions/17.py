n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
result = 0
while 1:
    if len(a) == 0 or (a[0] > k and a[-1] > k):
        break
    if a[0] <= k:
        result += 1
        a.pop(0)
    elif a[-1] <= k:
        result += 1
        a.pop(-1)
print(result)
