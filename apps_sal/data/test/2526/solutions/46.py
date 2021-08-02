x, y, a, b, c = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p2 = p[:x]
q2 = q[:y]
num = p2 + q2
num.sort()
ans = sum(num)
cnt = ans
for i in range(min(x + y, c)):
    cnt += r[i] - num[i]
    ans = max(ans, cnt)
print(ans)
