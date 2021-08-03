N = int(input())
N_List = list(map(str, input().strip()))
ans = 0
for i in range(1, N):
    c_ans = len(set(N_List[:i]) & set(N_List[i:]))
    if c_ans > ans:
        ans = c_ans
print(ans)
