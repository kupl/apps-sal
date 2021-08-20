(n, A) = map(int, input().split())
kosti = list(map(int, input().split()))
summ = 0
temp = 0
for i in kosti:
    summ += i
for i in kosti:
    temp = summ - i
    temp2 = min(A - (n - 1), i)
    ans = i - temp2 + max(0, A - temp - 1)
    print(ans, end=' ')
