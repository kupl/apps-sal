(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
f = True
for i in range(1, 10):
    if i in a and i in b:
        print(i)
        f = False
        break
if f:
    print(str(min(min(a), min(b))) + str(max(min(a), min(b))))
