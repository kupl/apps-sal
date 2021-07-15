input()

m = -1

for i, a in enumerate(map(int, input().split())):
    if a > m + 1:
        print(i+1)
        break
    else:
        m = max(m, a)
else:
    print(-1)

