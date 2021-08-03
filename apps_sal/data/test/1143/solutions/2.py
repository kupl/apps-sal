fin = open("input.txt", "r")
fout = open("output.txt", "w")
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
table = []
for i in range(int(fin.readline())):
    table.append([int(i) for i in fin.readline().split()])

ans = [0] * 500
for it in table:
    days = sum(day[0:it[0]]) + it[1] + 100
    for i in range(1, it[3] + 1):
        ans[days - i] += it[2]
print(max(ans), file=fout)
