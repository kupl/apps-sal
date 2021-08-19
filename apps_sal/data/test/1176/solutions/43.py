N = int(input())
a_ls = list(map(int, input().split()))
abs_ls = [0] * N
minus = 0
for i in range(N):
    if a_ls[i] < 0:
        minus += 1
    abs_ls[i] = abs(a_ls[i])
if minus % 2 == 1:
    ans = sum(abs_ls) - 2 * min(abs_ls)
else:
    ans = sum(abs_ls)
print(ans)
