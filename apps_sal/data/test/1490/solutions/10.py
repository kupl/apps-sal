n, m = map(int, input().split())
x = set(map(int, input().split()))
answer = []
i = 1
while True:
    if i > m:
        break
    if i in x:
        i += 1
        continue
    else:
        answer.append(i)
        m -= i
        i += 1
print(len(answer))
print(' '.join(map(str, answer)))
