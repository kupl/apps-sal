n = int(input())
a = list(map(int, input().split()))

len = -1
lastColor = -1
curLen = 0
a.append(-1)


for i in a:
    if i != lastColor:
        if len != -1:
            if curLen != len:
                print("NO")
                return
        else:
            if lastColor != -1:
                len = curLen
        lastColor = i
        curLen = 1
    else:
        curLen += 1

print("YES")
