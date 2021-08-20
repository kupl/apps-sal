(n, a) = map(int, input().split())
x = list(map(int, input().split()))
x = [i - a for i in x]
dic = {0: 1}
for i in x:
    for (j, k) in list(dic.items()):
        dic[i + j] = dic.get(i + j, 0) + k
print(dic[0] - 1)
