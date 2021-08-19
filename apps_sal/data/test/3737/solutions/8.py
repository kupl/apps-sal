n = int(input())
l = list(map(int, input().split()))
l.sort()
cnt = 0
for i in range(len(l)):
    if l[0] < l[i] < l[-1]:
        cnt += 1
print(cnt)
