inp = input().split()
n = int(inp[0])
s = int(inp[1])
start = s + 1
thresh = s + 500
ans = 0
if n > thresh:
    ans += n - thresh
else:
    thresh = n
val = 0
for i in range(start, thresh + 1):
    val = i
    while i > 0:
        val -= i % 10
        i = i // 10
    if val >= s:
        ans += 1
print(ans)
