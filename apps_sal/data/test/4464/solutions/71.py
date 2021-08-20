(a, b, c) = map(int, input().split())
bool = False
for i in range(1, 101):
    if a * i % b == c:
        bool = True
if bool:
    print('YES')
else:
    print('NO')
