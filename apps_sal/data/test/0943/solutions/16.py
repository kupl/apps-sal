n = int(input())
l = map(int, input().split())
l = sorted(l)
s = sum(l)

if (s % 2) == 1:
    for i in l:
        if (i % 2) == 1:
            s -= i
            break
print(s)
