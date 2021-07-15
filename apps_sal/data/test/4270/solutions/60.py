N = int(input())
v_list = list(map(int, input().split()))

v_list_min = sorted(v_list)
ans = v_list_min[0]
for i in range(1, N):
    ans = (ans + v_list_min[i])/2

print(ans)
