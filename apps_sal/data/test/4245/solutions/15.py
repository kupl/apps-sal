(A, B) = map(int, input().split())
num = 1
ans = 0
while True:
    if num >= B:
        break
    ans += 1
    num += A - 1
print(ans)
