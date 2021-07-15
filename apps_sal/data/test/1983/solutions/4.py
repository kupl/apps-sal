t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    set_ = set(a)
    print(len(set_))
