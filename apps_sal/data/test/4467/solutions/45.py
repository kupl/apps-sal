n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))
ab = sorted(ab, key=lambda x: x[1], reverse=True)
cd = []
for i in range(n):
    cd.append(list(map(int, input().split())))
cd = sorted(cd, key=lambda x: x[0])
ans = 0
for i in cd:
    for (ji, j) in enumerate(ab):
        if i[0] > j[0] and i[1] > j[1]:
            ans += 1
            ab.pop(ji)
            break
print(ans, flush=True)
