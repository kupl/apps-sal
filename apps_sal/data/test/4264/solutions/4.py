n = int(input())
if n < 10:
    print(n)
elif 10 <= n <= 99:
    print(9)
elif 100 <= n <= 999:
    print(n - 90)
elif 1000 <= n <= 9999:
    print(9 + 900)
elif 10000 <= n <= 99999:
    print(n - 9090)
elif 100000 <= n <= 100000:
    print(9 + 900 + 90000)
