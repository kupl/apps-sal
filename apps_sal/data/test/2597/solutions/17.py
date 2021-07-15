def check(ans):
    nonlocal  a
    cnt = 0
    for i in range(len(a)):
        if a[i] >= ans:
            cnt += 1
        else:
            break
    return cnt >= ans

k = int(input())
for i in range(k):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a = a[::-1]
    left = 1
    right = a[0]
    while (right - left) > 1:
        middle = (left + right) // 2
        if check(middle):
            left = middle
        else:
            right = middle
    if check(right):
        print(right)
    else:
        print(left)

