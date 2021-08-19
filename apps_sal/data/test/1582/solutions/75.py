from collections import defaultdict
N = int(input())
dic = defaultdict(int)
for i in range(1, N + 1):
    s = str(i)
    dic[s[0], s[-1]] += 1
ans = 0
for key in dic.keys():
    (a, b) = key
    if (b, a) in dic:
        ans += dic[a, b] * dic[b, a]
print(ans)
