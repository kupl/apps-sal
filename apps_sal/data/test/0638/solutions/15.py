(n, m) = map(int, input().split())
t = list(map(int, input().split()))
print(0, end=' ')
for i in range(1, len(t)):
    temp = sorted(t[:i])
    time = m - t[i]
    ptr = 0
    while ptr < i and time - temp[ptr] >= 0:
        time -= temp[ptr]
        ptr += 1
    print(i - ptr, end=' ')
print()
