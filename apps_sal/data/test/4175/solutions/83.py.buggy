N = int(input())
words = []

for i in range(N):
    W = input()
    if i == 0:
        top = W[-1]
        words.append(W)
    else:
        if top != W[0] or W in words:
            print("No")
            return
        else:
            top = W[-1]
            words.append(W)

print("Yes")
