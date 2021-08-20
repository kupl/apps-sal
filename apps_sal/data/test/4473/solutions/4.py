t = int(input())
for i in range(t):
    T = input().split(' ')
    (a, b, k) = (int(T[0]), int(T[1]), int(T[2]))
    s = (k // 2 + k % 2) * a - k // 2 * b
    print(s)
