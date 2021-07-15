n = int(input())
h = list(map(int, input().split()))
val = 0
for i in range(n):
    if val > h[i]:
        print("No")
        return
    else:
        val = max(val, h[i] - 1)

print("Yes")
