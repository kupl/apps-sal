S = list(input())
T = list(input())

count = 0
i = 0

for it in S:
    if(it == T[i]):
        count = count + 1
    i = i + 1

print(count)

