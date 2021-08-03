n = int(input())
AB = [list(map(int, input().split())) for i in range(n)]
AB.sort(key=lambda x: x[1])
t = 0
for ab in AB:
    t += ab[0]
    if t > ab[1]:
        print("No")
        break
else:
    print("Yes")
