#map(int, input().split())
def check(a):
    if a % 3 == 0 or a % 7 == 0:
        return True
    if a in [1, 2, 4, 5, 8, 11]:
        return False
    return True


n = int(input())
for i in range(n):
    x = int(input())
    if check(x):
        print('YES')
    else:
        print('NO')
