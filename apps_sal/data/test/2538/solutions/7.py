T = int(input())
for i in range(T):
    (s, i, e) = list(map(int, input().split()))
    if s > i + e:
        a = e + 1
    else:
        a = min((s + e - i - 1) // 2 + 1, e)
    if a <= 0:
        print(0)
    else:
        print(a)
