(n, k, q) = list(map(int, input().split()))
ans = [k - q] * n
for _ in range(q):
    a = int(input()) - 1
    ans[a] += 1
for i in range(n):
    print('Yes' if ans[i] > 0 else 'No')
