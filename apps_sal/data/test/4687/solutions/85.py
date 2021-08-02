n, k = map(int, input().split())
a_b = [list(map(int, input().split())) for _ in range(n)]
a_b = sorted(a_b, key=lambda x: x[0])

count = 0
for i in range(len(a_b)):
    a, b = a_b[i]
    count += b
    if count >= k:
        print(a)
        break
