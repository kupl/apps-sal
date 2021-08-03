n = int(input())
s = input()
a = [int(i) for i in s]
m = sum(a)
for i in range(2, n + 1):
    if m % i == 0:
        k = m // i
        summ = 0
        cnt = 0
        for i in range(n):
            summ += a[i]
            if summ == k:
                cnt += 1
                summ = 0
        if k * cnt == m:
            print("YES")
            return
print("NO")
