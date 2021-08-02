n = int(input())
ls = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a, b, c = ls[i], ls[j], ls[k]
            if (a + b > c and b + c > a and c + a > b) and (a != b and b != c and c != a):
                count += 1

print(count)
