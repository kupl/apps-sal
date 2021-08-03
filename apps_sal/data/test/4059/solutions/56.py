N = int(input())
count = 0
for A in range(1, 10**6 + 1):
    if A > N:
        break
    else:
        count += (N - 1) // A
print(count)
