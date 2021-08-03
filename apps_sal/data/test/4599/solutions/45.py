N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice_point = 0
Bob_point = 0

for i in range(N):
    if i % 2 == 0:
        Alice_point += a[0]
        a.pop(0)

    else:
        Bob_point += a[0]
        a.pop(0)

print(Alice_point - Bob_point)
