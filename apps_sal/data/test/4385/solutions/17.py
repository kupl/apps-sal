def f():
    x = [int(input()) for _ in range(5)]
    k = int(input())
    for i in range(5):
        for j in range(5):
            if abs(x[i] - x[j]) > k:
                return":("
    return "Yay!"
print(f())
