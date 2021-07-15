a, b, c = map(int, input().split())
judge=False
for i in range(b):
    if a*i%b==c:
        judge = True
        break

if judge:
    print("YES")
else:
    print("NO")
