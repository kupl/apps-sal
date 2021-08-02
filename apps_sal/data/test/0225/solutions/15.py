L = list(map(int, input().split()))
L.sort()
if (L[0] + L[-1] == L[1] + L[2] or L[0] + L[1] + L[2] == L[3]):
    print("YES")
else:
    print("NO")
