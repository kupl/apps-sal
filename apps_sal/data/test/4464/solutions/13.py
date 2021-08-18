a, b, c = list(map(int, input().split()))
count = 0
for i in range(b + 1):
    if ((i * a) % b) == c:
        print("YES")
        count += 1
        break
    else:
        pass

if count == 0:
    print("NO")
else:
    pass
