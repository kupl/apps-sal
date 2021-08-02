N = int(input())
L = list(map(int, input().split()))

x = sum(L)
for l in L:
    if l >= x - l:
        print("No")
        break
else:
    print("Yes")
