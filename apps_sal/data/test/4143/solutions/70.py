N = int(input())
T = []
for _ in range(5):
    T.append(int(input()))
print((N + min(T) - 1) // min(T) + 4)
