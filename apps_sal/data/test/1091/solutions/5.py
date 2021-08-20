__author__ = 'Administrator'
n = int(input())
test = []
test1 = []
test = list(map(int, input().split()))
i = 1
for value in test:
    test1.append((value, i))
    i += 1
test1.sort(key=lambda d: d[0], reverse=True)
print(test1[0][1], test1[1][0])
