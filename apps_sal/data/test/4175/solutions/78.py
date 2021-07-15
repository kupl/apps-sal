n = int(input())
w_l = [ input() for _ in range(n) ]
memo = set()
b_w = w_l[0][0]
ans = 'Yes'
for w in w_l:
    if b_w == w[0]:
        if w not in memo:
            memo.add(w)
            b_w = w[-1]
            continue
    ans = 'No'
    break
print(ans)
