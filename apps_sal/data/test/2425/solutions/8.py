import sys
input = sys.stdin.readline

q = int(input())
x = []
for i in range(q):
    v = int(input())
    tv = v
    cnt, len = 0, 0
    while tv > 0:
        if tv & 1:
            cnt += 1
        len += 1
        tv //= 2
    if cnt != len:
        print(2**len - 1)
    else:
        a = 1
        i = 2
        while i * i <= v:
            if v % i == 0:
                a = v // i
                break
            i += 1
        print(a)
