N = int(input())
H = map(int, input().split())
ans = 0
num = 0
for i in H:
    if num <= i:
        ans += 1
        num = i
print(ans)
