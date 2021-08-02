n = int(input())

data = []
for i in range(n):
    data.append(input())

res = -1
cur_res = 0

for i in range(ord('a'), ord('z') + 1):
    for j in range(i + 1, ord('z') + 1):
        for k in range(n):
            if data[k].count(chr(i)) + data[k].count(chr(j)) == len(data[k]):
                cur_res += len(data[k])
        res = max(res, cur_res)
        cur_res = 0

print(res)
