n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 200001
for x in a:
    cnt[x] += 1

mx = max(cnt)
val = -1
for x in a:
    if cnt[x] == mx:
        val = x

index = -1
for i, x in enumerate(a):
    if x == val:
        index = i
        break

answer = []
for i in reversed(list(range(index))):
    if a[i] > val:
        answer.append((2, i, i + 1))
    elif a[i] < val:
        answer.append((1, i, i + 1))

for i in range(index + 1, n):
    if a[i] > val:
        answer.append((2, i, i - 1))
    elif a[i] < val:
        answer.append((1, i, i - 1))

print(len(answer))
for a, b, c in answer:
    print(a, b + 1, c + 1)

