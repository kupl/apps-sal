from operator import itemgetter
n = int(input())
ai = list(map(int, input().split()))
ai2 = [[ai[i], i + 1] for i in range(n)]
ai2.sort(key=itemgetter(0))
ans = []
index = n - 1
index2 = 0
num = sum(ai)
while index2 < n and index > -1:
    temp = (num - ai2[index2][0]) / 2
    while index > -1 and temp < ai2[index][0]:
        index -= 1

    if temp == ai2[index][0]:
        if index == index2:
            if temp == ai2[index - 1][0]:
                ans += [ai2[index2][1]]
        else:
            ans += [ai2[index2][1]]
    index2 += 1
print(len(ans))
for i in ans:
    print(i, end=" ")
