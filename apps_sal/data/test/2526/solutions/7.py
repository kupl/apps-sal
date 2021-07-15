X, Y, A, B, C = map(int, input().split())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

p_list_max = sorted(p_list, reverse=True)
q_list_max = sorted(q_list, reverse=True)
r_list_max = sorted(r_list, reverse=True)

p_list_X = p_list_max[:X]
q_list_Y = q_list_max[:Y]

ans_list = []
ans_list.extend(p_list_X)
ans_list.extend(q_list_Y)
ans_list.extend(r_list_max)
ans_list_max = sorted(ans_list, reverse=True)

ans = 0
#print(p_list_X, q_list_Y, ans_list_max)
for i in range(X+Y):
    ans += ans_list_max[i]
print(ans)
