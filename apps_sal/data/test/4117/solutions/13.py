n = int(input())
L = sorted(list(map(int, input().split())))

cnt = 0
for i in range(n - 2):
    a = L[i]
    for j in range(i + 1, n - 1):
        b = L[j]
        if a != b:
            for k in range(j + 1, n):
                c = L[k]
                if a != c and b != c and a + b > c and b + c > a and c + a > b:
                    cnt += 1

print(cnt)
