N, K = map(int, input().split())
p = list(map(int, input().split()))
res_list = []

for i in p:
    r = int(i)
    res_list.append(r)

res_list.sort()
print(sum(res_list[0:K]))
