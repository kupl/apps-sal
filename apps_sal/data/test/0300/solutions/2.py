n = int(input())
ai = list(map(int, input().split()))
ai.sort()
summ = sum(ai)
if summ / n >= 4.5:
    print(0)
else:
    for i in range(n):
        summ += 5 - ai[i]
        if summ / n >= 4.5:
            print(i + 1)
            break
