a,b,k = list(map(int, input().split()))
ans = []
for i in range(k):
    n = a + i
    if n > b:
        break
    ans.append(n)

st = b - k + 1
st = max(st, ans[-1]+1)
for i in range(st, b+1):
    ans.append(i)

print(*ans, sep='\n')
