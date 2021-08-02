input()
a = list(map(int, input().split()))
b = min(a)
for i in a:
    if i % b:
        print(-1)
        break
else:
    print(b)
