n, m = list(map(int, input().split()))

for i in range(n):
    a = list(map(int, input().split()))
    if i == 0:
        answer = set(a[1:])
    else:
        answer = answer & set(a[1:])

print(len(answer))
