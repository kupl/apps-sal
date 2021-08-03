n = int(input())
clothes = {}
for i in range(n):
    size = input()
    if size not in clothes:
        clothes[size] = 0
    clothes[size] += 1

ans = 0
for i in range(n):
    size = input()
    if size not in clothes or clothes[size] == 0:
        ans += 1
    else:
        clothes[size] -= 1

print(ans)
