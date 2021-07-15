n = int(input())
al = []
for i in range(n):
    al.append(int(input()))

al.sort()
al.append(10**9+1)
cnt = 1
ans = 0
for j in range(n):
    if al[j] == al[j+1]:
        cnt += 1
    elif cnt%2 == 0:
        cnt = 1
    elif cnt%2 == 1:
        cnt = 1
        ans += 1
print(ans)
