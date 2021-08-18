
n = int(input())
s = list(input())

gr_lg = []
i = 0
while i < len(s):
    gr_cnt = 0
    while i < len(s) and s[i] == 'B':
        gr_cnt += 1
        i += 1
    if gr_cnt > 0:
        gr_lg.append(gr_cnt)
    i += 1

print(len(gr_lg))
for lg in gr_lg:
    print(lg, end=" ")
