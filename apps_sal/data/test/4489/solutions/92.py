from collections import defaultdict

cnt = defaultdict(int)
cnt["a" * 11] = 0
for _ in range(int(input())):
    cnt[input()] += 1
for _ in range(int(input())):
    cnt[input()] -= 1
ans = max(cnt.values())
print(ans)
