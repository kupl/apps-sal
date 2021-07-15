N = int(input())
dic, rst = {}, []
for i in range(N):
    key = input()
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
max_val = max(dic.values())
rst = [ key for key, value in dic.items() if value == max_val ]
[ print(i) for i in sorted(rst) ]
