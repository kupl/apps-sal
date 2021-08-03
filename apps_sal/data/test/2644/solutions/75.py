N = int(input())
P = list(map(int, input().split()))

ans = []
d = dict()
for i in range(N):
    d[P[i]] = i
num = 1
left = 0
s = set()
c = 0
while(num <= N):
    if num in s:
        if d[num] != num - 1:
            print(-1)
            return
    elif d[num] != num - 1:
        left = num - 1

        s.add(num)
        right = d[num]
        P[right] = P[right - 1]
        d[P[right]] = right
        ans.append(right)
        d[num] = num - 1
        for i in range(right - 2, left - 1, -1):
            s.add(P[i])
            d[P[i]] += 1
            ans.append(i + 1)
    num += 1
if len(ans) == N - 1:
    print(*ans, sep='\n')
else:
    print(-1)
