n = int(input())
d = {}
for i in range(n):
    d[input()] = i
answer = []
k = list(d.keys())
for i in range(len(k)):
    answer += [(d[k[i]], k[i])]
answer.sort(reverse=True)
for i in range(len(answer)):
    print(answer[i][1])
