t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = -1
    for i in range(n):
        if a[i] == b[i]:
            if diff == -1:
                continue
            else:
                diff = 10**9
        else:
            if diff == -1:
                diff = b[i] - a[i]
                if diff < 0:
                    print("NO")
                    break
            if diff != -1:
                if diff == b[i] - a[i]:
                    continue
                else:
                    print("NO")
                    break
    else:
        print("YES")
