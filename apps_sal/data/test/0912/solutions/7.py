t = int(input())
for _ in range(t):
    n, s, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = set(a)
    for i in range(0, 1005):
        if 1 <= s+i <= n:
            if s+i not in a:
                print(i)
                break
        if 1 <= s-i <= n:
            if s-i not in a:
                print(i)
                break
                 

