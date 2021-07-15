N = str(input())
N_list = list(N)
ans = 0

for i in range(len(N_list)):
    N_list[i] = int(N_list[i])
    ans += N_list[i]

if ans % 9 == 0:
    print("Yes")
else:
    print("No")
