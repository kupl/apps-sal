
inp = input().split()
n = int(inp[0])
k = int(inp[1])

s = input()

cnt = {}
for c in s:
    cnt[c] = cnt.get(c, 0) + 1

if(len(cnt) < k):
    print(0)
else:
    ans = cnt["A"]
    for c, v in cnt.items():
        ans = min(ans, v)
    print(ans * k)
