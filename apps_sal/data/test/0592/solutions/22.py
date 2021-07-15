n = int(input())
print(sum([i * (int(n / i) - 1) for i in range(2, n + 1)]) * 4)

# run : python wtf.py

