(a, b) = map(int, input().split())
(aq, bq) = (a % 4, b % 4)
ans = 0
for i in range(a, a + (4 - aq)):
    ans ^= i
for i in range(b - bq, b + 1):
    ans ^= i
print(ans)
