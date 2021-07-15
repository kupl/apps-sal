import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
    minx = {}
    maxx = {}
    miny = {}
    maxy = {}
    matrix = []
    for i in range(n):
        matrix.append(list(input().strip()))
    for i in range(n):
        for j in range(m):
            if matrix[i][j]!='.':
                try:
                    minx[matrix[i][j]] = min(minx[matrix[i][j]], j)
                except: minx[matrix[i][j]] = j
                try:
                    maxx[matrix[i][j]] = max(maxx[matrix[i][j]], j)
                except: maxx[matrix[i][j]] = j
                try:
                    miny[matrix[i][j]] = min(miny[matrix[i][j]], i)
                except: miny[matrix[i][j]] = i
                try:
                    maxy[matrix[i][j]] = max(maxy[matrix[i][j]], i)
                except: maxy[matrix[i][j]] = i
    copy = []
    for i in range(n):
        copy.append([])
        for j in range(m):
            copy[-1].append('.')
    for char in range(ord('a'), ord('z')+1):
        char = chr(char)
        try:
            if minx[char]==maxx[char]:
                c = minx[char]
                for r in range(miny[char], maxy[char]+1):
                    copy[r][c] = char
            else:
                r = miny[char]
                for c in range(minx[char], maxx[char]+1):
                    copy[r][c] = char
        except: pass
    if matrix==copy:
        print("YES")
        cnt = -1
        for char in range(ord('z'), ord('a')-1, -1):
            char = chr(char)
            try:
                minx[char]+=0
                break
            except: pass
        else: cnt = 0
        if cnt!=0:
            cnt = ord(char)-ord('a')+1
        print(cnt)
        ans = []
        for char in range(ord('a'), ord('a')+cnt):
            char = chr(char)
            try:
                ans.append((miny[char], minx[char], maxy[char], maxx[char]))
            except: pass
        i = 0
        for char in range(ord('a'), ord('a')+cnt):
            char = chr(char)
            print(ans[i][0]+1, ans[i][1]+1, ans[i][2]+1, ans[i][3]+1)
            try: minx[char]+=0; i+=1
            except: pass
    else:
        print("NO")

