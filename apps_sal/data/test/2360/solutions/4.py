t = int(input())
for i in range(t):
    n = int(input())
    students = []
    for i in range(n):
        students.append(list(map(int, input().split())))    
    time = 0
    ans = []
    for i in students:
        l = i[0]
        r = i[1]
        if r < time:
            ans.append(0)
            continue
        else:
            ans.append(max(time, l))
            time = max(time + 1, l + 1)
    print(*ans)
