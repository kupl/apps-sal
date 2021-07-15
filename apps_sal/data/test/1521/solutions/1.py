p, _= list(map(int, input().split()))

used = set()

for i in range(_):
    x = int(input())
    if x%p in used:
        print(i+1)
        return
    else:
        used.add(x%p)
print(-1)

