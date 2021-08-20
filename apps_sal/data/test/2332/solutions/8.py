(n, k, m) = list(map(int, input().strip().split(' ')))
wordlist = list(map(str, input().strip().split(' ')))
wordcost = list(map(int, input().strip().split(' ')))
l = list()
for i in range(k):
    newlist = list(map(int, input().strip().split(' ')))
    l.append(newlist[1:])
message = list(map(str, input().strip().split(' ')))
d = dict()
updcost = list()
for i in range(k):
    mini = float('inf')
    for ele in l[i]:
        mini = min(mini, wordcost[ele - 1])
    for ele in l[i]:
        d[wordlist[ele - 1]] = mini
s = 0
for ele in message:
    s += d[ele]
print(s)
