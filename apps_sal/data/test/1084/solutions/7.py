BLACK, WHITE = "#", "."
n, m = list(map(int, input().split()))
blacks = [{i for i, c in enumerate(input()) if c == BLACK} for i in range(n)]
answer = "Yes"
for i in range(n):
    for j in range(i):
        if blacks[i] & blacks[j] and blacks[i] != blacks[j]:
            answer = "No"
print(answer)
