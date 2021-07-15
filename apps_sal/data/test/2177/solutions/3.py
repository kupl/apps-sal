test = int(input())
for z in range(test):
    a, b = map(int, input().split())
    ans = 0
    current = 9
    while current <= b:
        if (current + 1 == 10 ** len(str(current))):
            ans += a
        current = current * 10 + 9
    print(ans)
