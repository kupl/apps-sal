from collections import Counter
ans = 0
_ = input()
a = list(map(int, input().split()))
for k,v in Counter(a).items():
    if k > v:
        ans += v
    elif k < v:
        ans += v-k
print(ans)
