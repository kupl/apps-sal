n, a, b = list(map(int, input().split()))
answ = 0
for fir in range(1, n):
    sec = n - fir
    answ = max(answ, min(a // fir, b // sec))
print(answ)
    

