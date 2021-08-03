N = int(input())
ans = {}
for i in range(N):
    A = input()
    if A in ans:
        ans[A] += 1
    else:
        ans[A] = 1
c = 0
for i in ans:
    if ans[i] % 2 == 1:
        c += 1
print(c)
