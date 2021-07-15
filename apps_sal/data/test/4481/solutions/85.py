N = int(input())
dic = {}
for i in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
max_val = max(dic.values())
rst = [ key for key, val in dic.items() if val == max_val ]
[ print(i) for i in sorted(rst) ]
