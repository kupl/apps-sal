h, n = list(map(int, input().split()))
a = list(map(int, input().split()))

hp = 0
result = 'No'

for i in range(n):
    hp = hp + a[i]
    if hp >= h:
        result = 'Yes'
        break

print(result)

