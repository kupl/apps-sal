k = int(input())
n = sorted(map(int, list(input())))
s = sum(n)
c = 0
if s < k:
    for i in n:
        s = s - i + 9
        c += 1
        if s >= k:
            break
print(c)

