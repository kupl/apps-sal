N, K = map(int, input().split())
p_list = list(map(int, input().split()))

p_list_E = []
p_list_E_temp = [1, 1.5, 2, 2.5, 3, 3.5]

for i in range(len(p_list)):
    p_list_E.append((p_list[i]+1)*0.5)
#print(p_list_E)

p_list_sum = [0]
for i in range(0,N):
    p_list_sum.append(p_list_sum[i]+p_list_E[i])
#print(p_list_sum)

ans = 0
for i in range(K,N+1):
    ans = max(ans, p_list_sum[i]-p_list_sum[i-K])
print(ans)
