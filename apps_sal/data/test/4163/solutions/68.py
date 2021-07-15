N = int(input())
cnt = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    if a == b:
        cnt += 1
        if cnt == 3:
            print("Yes")
            return
    else:
        cnt = 0
print("No")

