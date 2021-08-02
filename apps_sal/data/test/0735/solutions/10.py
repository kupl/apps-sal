def solve():
    n = int(input())
    a = list(map(int, input().split()))
    left, right = 0, 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            left = i
            break
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            right = i + 1
    t = sorted(a)
    a[left:right + 1] = reversed(a[left:right + 1])
    print('yes\n', left + 1, right + 1) if(a == t) else print('no\n')


solve()
