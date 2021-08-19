from collections import *
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    count = Counter(ai)
    mostc = count.most_common()
    num = mostc[0][0]
    numcount = mostc[0][1]
    ans = -1
    for num in count:
        if count[num] == numcount:
            count[num] = 0
            ans += 1
    divisions = numcount - 1
    temp = 0
    for i in list(count.values()):
        temp += i
        if temp >= divisions:
            temp -= divisions
            ans += 1
    print(ans)
