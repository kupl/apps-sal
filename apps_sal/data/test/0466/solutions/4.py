c, d = list(map(int, input().split()))
n, m = list(map(int, input().split()))
f = n * m
k = int(input())
result = 0
uch = k

useosn = usedop = 0

while uch < f:
    if f-uch >= n:
        if c/n < d:
            result += c
            uch += n
        else:
            result += d
            uch += 1
    else:
        if c > (d*(f-uch)):
            while uch < f:
                result += d
                uch += 1
        else:
            result += c
            uch += n

print(max(0, result))




