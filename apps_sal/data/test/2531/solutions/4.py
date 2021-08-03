N = int(input())
numbs = []
dic = {}
e1 = set()
for i in range(N):
    numbs.append(int(input()))
    dic[numbs[i]] = 0
    e1.add(numbs[i])
for i in range(N):
    dic[numbs[i]] = dic[numbs[i]] + 1
s = set()
avg_ele = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        avg = (numbs[i] + numbs[j]) / 2
        if avg in e1 and avg not in s:
            avg_ele += dic[avg]
            s.add(avg)
print(avg_ele)
