N = int(input())
work = []
for _ in range(N):
    a, b = map(int, input().split())
    work.append((a, b))

work = sorted(work, key=lambda x: x[1], reverse=False)

result = 'Yes'
t = 0
for i, j in work:
    t += i
    if t > j:
        result = 'No'
        break
print(result)
