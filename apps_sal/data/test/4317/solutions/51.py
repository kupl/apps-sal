def my_input():
    return list(map(int, input().split()))


(a, b) = my_input()
print(max(a - b, max(a * b, a + b)))
