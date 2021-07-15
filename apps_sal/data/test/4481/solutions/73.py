N = int(input())
dic = {}
max_count = 1

for i in range(N):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
        if max_count < dic[s]:
            max_count = dic[s]

ans_lis = []

for i, j in dic.items():
    if j == max_count:
        ans_lis.append(i)

ans_lis.sort()

for i in ans_lis:
    print(i)
