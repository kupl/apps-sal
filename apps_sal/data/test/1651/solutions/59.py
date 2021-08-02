S, P = list(map(int, input().split()))

i = 1
while i * i <= P:
    if P % i == 0 and i + P // i == S:
        print("Yes")
        return
    i += 1
print("No")
