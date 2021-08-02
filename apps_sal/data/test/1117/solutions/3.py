amount = int(input())
prev_min = 10**10
for i in range(amount):
    h1, h2 = (int(i) for i in input().split())
    h1, h2 = max(h1, h2), min(h1, h2)
    if h1 <= prev_min:
        prev_min = h1
    elif h2 <= prev_min:
        prev_min = h2
    else:
        print("NO")
        return

print("YES")
