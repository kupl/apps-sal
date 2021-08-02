n = int(input())
L = list(map(int, input().split()))
m = 0
cnt = 0
for l in L:
    if m <= l:
        m = l
        cnt += 1
print(cnt)
