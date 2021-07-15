n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
ans = []
val = 0
for arr in a:
    for s in range(m):
        val += arr[s]*b[s]
        if s == m-1:
            ans.append(val)
            val = 0
ans = list(map(lambda x: x + c, ans))
print(sum(l > 0 for l in ans))
