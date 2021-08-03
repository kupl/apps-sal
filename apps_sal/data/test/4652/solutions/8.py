q = int(input())
while q:
    n = int(input())
    a = list(map(int, input().split()))
    a += a
    p = [i for i in range(1, n + 1)]
    flag = False
    for i in range(n):
        if a[i: i + n] == p or a[i: i + n] == p[::-1]:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")
    q -= 1
