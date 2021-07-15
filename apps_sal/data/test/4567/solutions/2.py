n = int(input())
s_l = [ int(input()) for _ in range(n) ]
s_l = sorted(s_l)

if sum(s_l)%10 != 0:
    ans = sum(s_l)
else:
    ans = 0
    base_ans = sum(s_l)
    for i in range(n):
        if (base_ans-s_l[i])%10 != 0:
            ans  = max(base_ans-s_l[i], ans)
print(ans)
