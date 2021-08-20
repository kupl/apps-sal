N = int(input())
K = int(input())
start = 1
for i in range(N):
    start_a = start * 2
    start_b = start + K
    if start_a <= start_b:
        start = start_a
    else:
        start = start_b
print(start)
