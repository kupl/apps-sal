N, A, B = map(int, input().split())
con = 0
for i in range(1, N + 1):
    a1 = i // 10000
    a2 = (i - a1 * 10000) // 1000
    a3 = (i - a1 * 10000 - a2 * 1000) // 100
    a4 = (i - a1 * 10000 - a2 * 1000 - a3 * 100) // 10
    a5 = i % 10
    if A <= a1 + a2 + a3 + a4 + a5 <= B:
        con += i
print(con)
