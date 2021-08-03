N = int(input())
answer = "No"
for i in range(1, 10):
    if N % i == 0:
        A = N // i
        if A < 10:
            answer = "Yes"

print(answer)
