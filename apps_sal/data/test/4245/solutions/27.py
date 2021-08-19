(A, B) = map(int, input().split())
cnt = 1
total = A
if B == 1:
    print(0)
else:
    while total < B:
        total += A - 1
        cnt += 1
    print(cnt)
