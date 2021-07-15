t = int(input())
answer = []
for kek in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] <= i+1:
            ans = i + 2
    answer.append(ans)
print(*answer,sep='\n')

