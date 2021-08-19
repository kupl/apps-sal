(N, A, B) = map(int, input().split())
Sum = 0
for i in range(N):
    o = (i + 1) // 10000
    a = (i + 1) % 10000 // 1000
    b = (i + 1) % 1000 // 100
    c = (i + 1) % 100 // 10
    d = (i + 1) % 10
    e = o + a + b + c + d
    if e >= A and e <= B:
        Sum = Sum + (i + 1)
print(Sum)
