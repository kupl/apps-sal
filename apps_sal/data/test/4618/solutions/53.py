S = list(input())
n = len(S)
k = int(input())
H = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
p = 0
cnt = 0
D = set()

while True:
    for i in range(n):
        if S[i] == H[p]:
            for j in range(1, 6):
                if i + j <= n:
                    D.add("".join(S[i:i + j]))

    p += 1
    if len(list(D)) >= k:
        break

D = list(D)
D.sort()

print(D[k-1])
