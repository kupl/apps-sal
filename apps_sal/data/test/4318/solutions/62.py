N = input()
H = map(int, input().split())

num = 0
ans = 0

for i in H:
    if num <= i:
        ans += 1
        num = i
print(ans)
