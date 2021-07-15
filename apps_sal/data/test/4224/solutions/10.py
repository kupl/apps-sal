
N = int(input())
l = list(map(int,input().split()))

ans = 0
for i in l:
    while i % 2 == 0:
        i /= 2
        ans += 1

print((int(ans)))

