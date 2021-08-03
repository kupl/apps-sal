
for c in range(int(input())):
    N = int(input())
    counter = 0
    segments = []
    for n in range(N):
        l, r = map(int, input().split())
        segments.append([[l, r], counter])
        counter += 1

    segments.sort()
    ans = [-1] * N

    rightBound = segments[0][0][1]
    valid = -1
    for i in range(1, len(segments)):
        if segments[i][0][0] > rightBound:
            valid = i
            break
        else:
            rightBound = max(rightBound, segments[i][0][1])

    if valid == -1:
        print(-1)
    else:
        for i in range(valid):
            ans[segments[i][1]] = 1
        for i in range(valid, len(segments)):
            ans[segments[i][1]] = 2

        for a in ans:
            print(a, end=' ')
    print()
'''
3
2
5 5
2 3
3
3 5
2 3
2 3
3
3 3
4 4
5 5
'''
