n = int(input())
s = sum(map(int, input().split()))
m = int(input())
st = False
for i in range(m):
    (l, r) = map(int, input().split())
    if s <= r:
        print(max(l, s))
        st = True
        break
if not st:
    print(-1)
