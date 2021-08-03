N = int(input())

current_doublet_count = 0
for i in range(N):
    d1, d2 = map(int, input().split(" "))
    if (d1 == d2):
        current_doublet_count += 1
        if (current_doublet_count >= 3):
            break
    else:
        current_doublet_count = 0

print("Yes" if current_doublet_count >= 3 else "No")
