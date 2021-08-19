(n, m, k) = list(map(int, input().split()))
hole = [False for _ in range(n)]
for h in input().split():
    hh = int(h) - 1
    hole[hh] = True
bone = 0
fallen = hole[0]
for _ in range(k):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    if not fallen:
        if bone == a:
            bone = b
        elif bone == b:
            bone = a
        fallen = hole[bone]
print(bone + 1)
