def check(n, lst, lk):
    lst[0] += lk
    for i in range(1, n):
        if lst[i] >= lst[0]:
            lk -= lst[i] - lst[0] + 1
    if lk >= 0:
        return True
    return False
n = int(input())
lst = list(map(int, input().split()))
left = -1
right = 100000
while left + 1 < right:
    middle = (left + right) // 2
    if check(n, lst.copy(), middle):
        right = middle
    else:
        left = middle
print(right)
            

