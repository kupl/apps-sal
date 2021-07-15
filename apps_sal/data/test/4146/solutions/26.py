from collections import Counter

n = int(input())
v = list(map(int, input().split()))

if len(set(v)) <= 1:
    print((int(n/2)))
    return

odd = [v[i] for i in range(0, n, 2)]
odd_val, odd_cnt = list(zip(*Counter(odd).most_common()))

even = [v[i] for i in range(1, n, 2)]
even_val, even_cnt = list(zip(*Counter(even).most_common()))

if even_val[0] != odd_val[0]:
    ans = n-even_cnt[0]-odd_cnt[0]
else:
    if (even_cnt[0] + odd_cnt[1]) >= (even_cnt[1] + odd_cnt[0]):
        ans = n-even_cnt[0]-odd_cnt[1]
    else:
        ans = n-even_cnt[1]-odd_cnt[0]
print(ans)

