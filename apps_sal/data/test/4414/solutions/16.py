t = int(input())
answer = []

for i in range (t):
    a, b, n, s = list(map(int,input().split()))
    ans = "NO"
    if a * n + b >= s:
        s %= n
        if s <= b:
            ans = "YES"
    answer.append(ans)
for i in range (t):
    print (answer[i])
