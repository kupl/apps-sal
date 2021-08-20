n = int(input())
a = tuple(map(int, input().split()))
A = sum(a)
found = False
m = int(input())
for i in range(m):
    (left, right) = list(map(int, input().split()))
    if left <= A <= right or A < left:
        print(max(left, A))
        found = True
        break
if not found:
    print(-1)
