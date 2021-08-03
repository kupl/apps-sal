x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

ans = 0
d_ans = 101

for i in range(-1, 102):
    for j in p:
        if i == j:
            break
    else:
        d = abs(x - i)
        if d_ans > d:
            ans = i
            d_ans = d
        elif d_ans == d and ans > i:
            ans = i

print(ans)
