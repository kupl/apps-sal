n = int(input())
w = sorted(list(map(int, input().split())), reverse=True)
h = sum(w) // 2
ans = 0
for i in w:
    if h >= ans + i:
        ans += i
    if h == ans:
        print("YES")
        break
if h != ans:
    print("NO")

