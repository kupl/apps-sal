t = int(input())
for _ in range(t):
    n = int(input())
    set_ = set()
    for i in range(1, int(n**0.5) + 10):
        set_.add(n // i)
    li = sorted(list(set_))
    num = li[0]
    li2 = [i for i in range(num)]
    print(len(li2) + len(li))
    print(*li2 + li)
