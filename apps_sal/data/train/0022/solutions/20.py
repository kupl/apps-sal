t = int(input())
for _ in range(t):
    a, k = list(map(int, input().split()))
    for i in range(k - 1):
        a += int(min(str(a))) * int(max(str(a)))
        if '0' in str(a):
            break
    print(a)
