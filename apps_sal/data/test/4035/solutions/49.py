(A, B) = list(map(int, input().split()))
for x in range(1, 10 ** 5):
    if 8 * x // 100 == A and 10 * x // 100 == B:
        print(x)
        break
else:
    print(-1)
