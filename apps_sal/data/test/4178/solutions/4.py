n = int(input())
h = list(map(int, input().split()))
check = True
for i in range(1, n):
    if h[i] >= h[i - 1]:
        continue
    elif h[i] + 1 == h[i - 1]:
        h[i] += 1
    else:
        check = False
        break
print("Yes" if check else "No")
