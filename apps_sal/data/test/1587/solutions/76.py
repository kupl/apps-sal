n = int(input())
li_c = input()
r_index = [i for (i, x) in enumerate(li_c) if x == 'R']
w_index = [i for (i, x) in enumerate(li_c) if x == 'W']
r_num = len(r_index)
w_num = len(w_index)
R = r_num
W = 0
ans = max(R, W)
for i in range(n):
    if li_c[i] == 'R':
        R -= 1
    else:
        W += 1
    ans = min(ans, max(R, W))
print(ans)
