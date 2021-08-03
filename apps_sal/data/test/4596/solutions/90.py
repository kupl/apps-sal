N = int(input())
li = list(map(int, input().split()))

flag = True
ans = -1

while(flag):
    ans += 1
    newlist = []
    for i in li:
        newlist.append(i // 2)
        if i % 2 != 0:
            flag = False
    li = newlist
print(ans)
