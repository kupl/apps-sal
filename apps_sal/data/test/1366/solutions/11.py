n = int(input())
O = [0] * n
B = list(O)
for i in range(n):
    a, b = list(map(int, input().split()))
    O[i] = b
    B[i] = a
ans = n
for i in range(n):
    for j in range(n):
        if(j == i):
            continue
        if(O[j] == B[i]):
            ans -= 1
            break
print(ans)
