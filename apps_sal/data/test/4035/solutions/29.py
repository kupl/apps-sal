(A, B) = map(int, input().split())
for i in range(1, 1001):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        print(i)
        break
else:
    print(-1)
