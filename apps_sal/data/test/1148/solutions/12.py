n = int(input())
a = list(map(int, input().split()))
minimum = min(a)
maximum = 0
ans = 0
ind = 0
challengers = []
for i in range(n):
    if a[i] != minimum and a[i - 1] == minimum:
        challengers.append(i)
while challengers:
    cnt = 0
    num = challengers.pop()
    similar = num
    while a[similar] != minimum:
        cnt += 1
        similar = (similar + 1) % n
    if cnt > maximum:
        maximum = cnt
        ind = num
ans = minimum * n
while a[ind] != minimum:
    ans += 1
    ind = (ind + 1) % n
print(ans)
