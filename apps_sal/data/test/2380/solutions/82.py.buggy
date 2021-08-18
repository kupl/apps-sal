n, m = list(map(int, input().split()))

a_list = list(map(int, input().split()))
a_list = sorted(a_list)
# print(a_list)
dic = {}

for _ in range(m):
    b, c = list(map(int, input().split()))
    dic[c] = dic.get(c, 0) + b

count = 0
for c in sorted(dic, reverse=True):
    for _ in range(dic[c]):
        if a_list[count] < c:
            a_list[count] = c
        else:
            print((sum(a_list)))
            return
        count += 1
        if count == n:
            print((sum(a_list)))
            return

print((sum(a_list)))
