s = set()
n = int(input())
m = input()
m = m.split()
cnt = 0
max_cnt = 0
for i in range(len(m)):
    if m[i] in s:
        s.remove(m[i])
        cnt -= 1
    else:
        s.add(m[i])
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)

