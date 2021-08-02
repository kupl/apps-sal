n, k = list(map(int, input().split()))

d = list(map(int, input().split()))

in_list = set()

con = []

for x in d:
    if x in in_list:
        continue
    if len(con) == k:
        top = con[0]
        in_list.remove(top)
        con.pop(0)

    con.append(x)
    in_list.add(x)

print(len(con))
print(*con[::-1])
