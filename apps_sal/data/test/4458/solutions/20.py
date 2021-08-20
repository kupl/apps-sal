n = int(input())
pn = [int(num) for num in input().split()]
maxpj = n + 1
answer = 0
for pi in pn:
    if pi < maxpj:
        answer += 1
        maxpj = pi
print(answer)
