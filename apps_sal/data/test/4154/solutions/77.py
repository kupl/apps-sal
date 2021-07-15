n, m = map(int, input().split())
l_r = [ list(map(int, input().split())) for _ in range(m) ]

l_ans = 0
r_ans = float('inf')
for l, r in l_r:
    l_ans = max(l_ans, l)
    r_ans = min(r_ans, r)
if r_ans < l_ans:
    ans = 0
else:
    ans = r_ans-l_ans+1
print(ans) 
