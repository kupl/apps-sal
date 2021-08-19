N = input().rstrip()
Ls = list(map(int, input().split()))
Ls.sort(reverse=True)


# print(Ls)
totalBarLength = 0
for i in range(0, len(Ls), 2):
    barLength = Ls[i + 1]
    totalBarLength += barLength
print(totalBarLength)
