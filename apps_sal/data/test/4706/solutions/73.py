c_lst = [str(input()) for _ in range(3)]
ans = ''
for i in range(3):
    ans += c_lst[i][i]
print(ans)
