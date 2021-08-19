# int(input())
# map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
n = int(input())
ai = [0] + list(map(int, input().split())) + [1001]
ans = 0
num = 1
for i in range(1, n + 2):
    if ai[i] == ai[i - 1] + 1:
        num += 1
    else:
        ans = max(ans, num - 2)
        num = 1
print(max(ans, num - 2))
