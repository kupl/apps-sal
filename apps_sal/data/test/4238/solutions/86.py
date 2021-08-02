N = input()
n = len(N)
N_lis = list(N)
ans = 0
for i in range(n):
    ans += int(N_lis[i])
if ans % 9 == 0:
    print("Yes")
else:
    print("No")
