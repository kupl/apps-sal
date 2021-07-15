n = int(input())
s = list(map(int, input().split()))

if s[0] % 2 == 0:
    for i in range(n):
        if s[i] % 2 == 1:
            print(" ".join(map(str, sorted(s))))
            return
    print(" ".join(map(str, s)))
    return
else:
    for i in range(n):
        if s[i] % 2 == 0:
            print(" ".join(map(str, sorted(s))))
            return
    print(" ".join(map(str, s)))
    return

