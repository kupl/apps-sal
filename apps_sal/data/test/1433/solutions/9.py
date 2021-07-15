a, b = map(int, input().split())
scene = [list(map(int, input().split())) for i in range(a)]
ans = 0
for i in range(a):
    first = 0
    between = 0
    last = 0    
    isactor = False
    for j in range(b):
        if scene[i][j] == 0 and isactor == False:
                first += 1
        elif isactor == True and scene[i][j] == 0:
            last += 1
        elif isactor == True and scene[i][j] == 1:
            between += last
            last = 0
        elif isactor == False and scene[i][j] == 1:
            isactor = True
    if isactor == True:
        ans += first + 2 * between + last
for j in range(b):
    first = 0
    between = 0
    last = 0    
    isactor = False
    for i in range(a):
        if scene[i][j] == 0 and isactor == False:
            first += 1
        elif isactor == True and scene[i][j] == 0:
            last += 1
        elif isactor == True and scene[i][j] == 1:
            between += last
            last = 0
        elif isactor == False and scene[i][j] == 1:
            isactor = True
    if isactor == True:
        ans += first + 2 * between + last  
print(ans)
