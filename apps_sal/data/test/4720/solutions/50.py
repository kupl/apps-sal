#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


n = int(input())

ans = 0

for i in range(n):
    l, r = list(map(int, input().split()))
    ans += r - l + 1
print(ans)
