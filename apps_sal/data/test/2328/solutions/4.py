import sys
input = sys.stdin.readline


t = int(input())
li = [list(map(int, input().split())) for i in range(2*t)]
for i in range(t):
    n, k = li[i*2][0], li[i*2][1]
    ans = 10**10
    j = 0
    item = 0
    while j + k < n:
        if -((-(li[i*2+1][j+k] - li[i*2+1][j])) // 2) < ans:
            ans = -((-(li[i*2+1][j+k] - li[i*2+1][j])) // 2)
            item = (li[i*2+1][j+k] + li[i*2+1][j])//2
        j += 1
    print(item)


