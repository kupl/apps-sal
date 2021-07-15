n, q = map(int, input().split())
s = input()
num_list = [list(map(int, input().split())) for _ in range(q)]
cnt = 0
cnt_list = [0]

for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'C':
        cnt += 1
        cnt_list.append(cnt)
    else:
        cnt_list.append(cnt)

for i in range(q):
    print(cnt_list[num_list[i][1]-1] - cnt_list[num_list[i][0]-1])
