n = int(input())
an = list(map(int, input().split()))
an.sort()

for x in range(n - 1):
    if an[x + 1] - an[x] == 0:
        print("NO")
        break

else:
    print("YES")
