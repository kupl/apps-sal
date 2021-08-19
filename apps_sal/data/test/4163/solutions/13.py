def judge():
    cnt = 0
    for _ in range(N):
        (x, y) = map(int, input().split())
        if x == y:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False


N = int(input())
if judge():
    print('Yes')
else:
    print('No')
