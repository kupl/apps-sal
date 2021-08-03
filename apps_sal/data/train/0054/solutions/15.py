q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    beki = [0] * 50
    for i in range(n):
        beki[s[i].bit_length() - 1] += 1

    for i in range(29):
        beki[i + 1] += beki[i] // 2

    if beki[11] > 0:
        print("YES")
    else:
        print("NO")
