N = int(input())
P = list(map(int, input().split()))

ls = [""] * N
cnt = 0

for i in range(N):
    if P[i] == i + 1:
        ls[i] = "#"
    else:
        ls[i] = "."

if ls[-1] == "#":
    if ls[-2] == "#":
        ls[-1], ls[-2] = ".", "."
    else:
        ls[-1] = "."
    cnt += 1

for j in range(N - 1):
    if ls[j] == "#":
        if ls[j + 1] == "#":
            ls[j + 1] = "."
        cnt += 1

print(cnt)
