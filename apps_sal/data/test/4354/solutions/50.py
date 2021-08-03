n, m = list(map(int, input().split()))
stu = []
checkpoints = []
for _ in range(n):
    ab = list(map(int, input().split()))
    stu.append(list(ab))
for _ in range(m):
    cd = list(map(int, input().split()))
    checkpoints.append(list(cd))

for s in stu:
    checkpoint_id = 1010101
    manhatttaaann_dis = 2 * (10**18) + 101010101
    for i, cp in enumerate(checkpoints):
        dist = abs(s[0] - cp[0]) + abs(s[1] - cp[1])
        if dist < manhatttaaann_dis:
            manhatttaaann_dis = dist
            checkpoint_id = i
    print((checkpoint_id + 1))
