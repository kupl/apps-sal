(A, B, T) = [int(v) for v in input().split(' ')]
T += 0.5
total = 0
time = A
while True:
    if time < T:
        total += B
        time += A
    else:
        break
print(total)
