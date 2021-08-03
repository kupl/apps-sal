t = int(input())
while(t):
    t -= 1
    co = [0] * 26
    n, m = list(map(int, input().split()))
    reco = [0] * n
    s = input()
    a = list(map(int, input().split()))
    for i in range(m):
        reco[0] += 1
        reco[a[i]] += -1
    reco[0] += 1
    for i in range(1, n):
        reco[i] = reco[i] + reco[i - 1]
    for i in range(n):
        z = ord(s[i]) - 97
        co[z] += reco[i]
    print(*co)
