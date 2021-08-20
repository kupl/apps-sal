n = int(input())
a = [int(_) for _ in input().split()]
cnt = [0 for i in range(max(a) + 1)]
for i in a:
    cnt[i] += 1
print('Bob' if cnt[min(a)] > n >> 1 else 'Alice')
