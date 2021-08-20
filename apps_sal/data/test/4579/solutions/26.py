N = int(input())
dic = {}
for i in range(N):
    s = str(input())
    if s not in dic:
        dic[s] = 'o'
print(len(dic))
