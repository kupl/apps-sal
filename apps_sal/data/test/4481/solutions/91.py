N = int(input())
dic = {}
for i in range(N):
    s = str(input())
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
S = sorted(dic.values())
t = S[-1]
X = []
for key in dic:
    if dic[key] == t:
        X.append(key)
x = sorted(X)
for i in range(len(X)):
    print(x[i])
