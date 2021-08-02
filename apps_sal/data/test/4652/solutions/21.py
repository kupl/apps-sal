t = int(input())

while t:
    t -= 1
    n = int(input())
    arr = [int(item) for item in input().split(' ')]
    ans = True
    for i in range(n):
        if (arr[i - 1] + 1) % n == arr[i] % n:
            continue
        ans = False
        break

    ans2 = True
    for i in range(n):
        if (arr[i] + 1) % n == arr[i - 1] % n:
            continue
        ans2 = False
        break
    print("YES" if ans or ans2 else "NO")
