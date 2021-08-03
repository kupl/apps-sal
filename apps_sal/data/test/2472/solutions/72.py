N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1])
cnt = 0
for a, b in AB:
    cnt += a
    if cnt > b:
        print("No")
        return
print("Yes")
