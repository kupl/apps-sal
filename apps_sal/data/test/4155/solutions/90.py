N = int(input())
h = [int(i) for i in input().split()]
ans = 0
count = 0


while h != [0] * N:
    f = False
    count = 0
    for i in range(N):
        if h[i] != 0 and f == False:
            f = True
            count += 1
        if h[i] == 0 and f == True:
            f = False

    ans += count
    for i in range(N):
        h[i] = max(h[i] - 1, 0)

print(ans)
