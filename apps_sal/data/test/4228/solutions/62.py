# nはりんごの数　りんごiの味はl＋i-1

n, l = map(int, input().split())

each_taste = []
for x in range(1, n + 1):
    each_taste.append(l + x - 1)

if min(each_taste) >= 0:
    print(sum(each_taste[1:]))

elif max(each_taste) >= 0:
    print(sum(each_taste))

else:
    print(sum(each_taste[:-1]))
