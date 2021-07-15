h, w = map(int, input().split())
c_lst = [list(map(str, input().split())) for _ in range(h)]

new_lst = []
for i in range(h):
    new_lst.append(c_lst[i])
    new_lst.append(c_lst[i])

for i in range(len(new_lst)):
    new = new_lst[i][0]
    print(new)
