import sys
input = sys.stdin.readline
q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    odd = 0
    for j in range(n):
        if a[j] % 2 != 0:
            odd += 1
    if odd < k:
        print('NO')
    elif odd > k and (odd - k) % 2 != 0:
        print('NO')
    else:
        print('YES')
        ans = []
        for j in range(n):
            if len(ans) == k - 1:
                ans.append(n)
                break
            if a[j] % 2 != 0:
                ans.append(j + 1)
        print(*ans)
