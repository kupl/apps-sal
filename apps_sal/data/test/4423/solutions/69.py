n = int(input())
list_res = []
for i in range(0, n):
    (s, p) = input().split()
    list_res.append([s, int(p), i + 1])
list_res_point = sorted(list_res, key=lambda x: x[1], reverse=True)
list_ans = sorted(list_res_point, key=lambda x: x[0])
for i in range(0, n):
    print(list_ans[i][2])
