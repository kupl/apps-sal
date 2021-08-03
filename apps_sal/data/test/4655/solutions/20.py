q = int(input())
for _ in range(q):
    a, b, c = list(map(int, input().split()))
    sum = a + b + c
    print(sum // 2)
