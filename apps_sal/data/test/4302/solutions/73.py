number = input().split(" ")
A = int(number[0])
B = int(number[1])

ans = 0

for i in range(2):
    if A >= B:
        ans += A
        A -= 1
    else:
        ans += B
        B -= 1

print(ans)
