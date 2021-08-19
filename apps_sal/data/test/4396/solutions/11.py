#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

ans = 0

for i in range(n):
    if l[i][1] == "JPY":
        ans += int(l[i][0])
    else:
        ans += float(l[i][0]) * 380000.0
print(ans)
