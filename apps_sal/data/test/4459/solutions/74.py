from collections import Counter
ans = 0
_ = input()
a = Counter(map(int, input().split()))
for k,v in a.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v-k
print(ans)
