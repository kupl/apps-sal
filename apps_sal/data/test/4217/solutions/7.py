n, m = map(int, input().split())

dic = {}

for i in range(n):
    k_list = [int(i) for i in input().split()]
    k = k_list[0]
    a_list = k_list[1:]

    for j in a_list:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

value_list = list(dic.values())
ans = value_list.count(n)

print(ans)
