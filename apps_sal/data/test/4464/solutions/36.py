a, b, c = map(int, input().split())
count = 1
while a*count % b != 0:
    count += 1
for i in range(count):
    if a*i%b == c:
        print("YES")
        return
print("NO")
