_ = input()
a = list(map(int, input().split(' ')))
fin_ans = 1
ans = 1
b = a[0]
for i in a[1:]:
    if b < i:
        ans += 1
    else:
        fin_ans = max(ans, fin_ans)
        ans = 1
    b = i

print(max(fin_ans, ans))
