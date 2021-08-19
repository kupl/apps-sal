(A, B) = map(int, input().split())
a = A % 4
b = B % 4
ans = 0
cnt = 0
for i in range(a, 4):
    ans = ans ^ A + cnt
    cnt += 1
cnt = 0
for i in range(b, -1, -1):
    ans = ans ^ B - cnt
    cnt += 1
print(ans)
