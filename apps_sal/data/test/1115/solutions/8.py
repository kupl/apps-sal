n = int(input())
st = sum(map(int, input().split()))
m = int(input())
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    if st < a:
        print(a)
        break
    elif st <= b:
        print(st)
        break
else:
    print('-1')
