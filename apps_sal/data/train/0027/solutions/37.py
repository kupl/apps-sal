t = int(input())
ans_l = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ar = set()
    for i in a:
        if i % 2 == 0:
            x = i
            ar.add(x)
            while x % 2 == 0:
                ar.add(x)
                x //= 2
    ans_l.append(len(ar))
print(*ans_l, sep='\n')
