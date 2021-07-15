n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
food = 0
manzoku = 0
bonus = 0
before = 10*3
ans = 0
for i in range(n):
    food = a[i]
    manzoku = b[food-1]
    if food == before+1:
        bonus = c[food-2]
        ans += manzoku + bonus
    else:
        ans += manzoku
    before = food
print(ans)
