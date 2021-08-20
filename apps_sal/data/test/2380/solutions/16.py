from collections import Counter
(n, m) = list(map(int, input().split()))
lis = list(map(int, input().split()))
cnt = Counter(lis)
for _ in range(m):
    (b, c) = list(map(int, input().split()))
    cnt[c] += b
anslis = sorted(list(cnt.items()), key=lambda x: x[0], reverse=True)
ans = 0
for (key, value) in anslis:
    if n > value:
        ans += key * value
        n -= value
    else:
        ans += n * key
        print(ans)
        break
