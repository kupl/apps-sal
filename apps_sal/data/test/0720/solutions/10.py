n = int(input())
a0, b0 = list(map(int, input().split()))
wynik = min(a0, b0) + 1
for i in range(n - 1):
    a1, b1 = list(map(int, input().split()))
    wynik += max(0, max(0, 1 + min(a1, b1) - max(a0, b0)))
    if a0 == b0:
        wynik -= 1
    a0 = a1
    b0 = b1
print(wynik)
