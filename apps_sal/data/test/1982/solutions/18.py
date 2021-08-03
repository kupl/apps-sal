n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))

    if (a - b) % 2 == 0 and b <= int(a**0.5):
        print("YES")
    else:
        print("NO")
