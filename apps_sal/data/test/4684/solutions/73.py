r, g, b = list(map(str, input().split()))
li = r + g + b

if int(li) % 4 == 0:
    print("YES")
else:
    print("NO")
