q = int(input())
while q:
    (a, b, c) = list(map(int, input().split()))
    A = [a, b, c]
    print(sum(A) // 2)
    q = q - 1
