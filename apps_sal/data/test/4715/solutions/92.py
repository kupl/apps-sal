a, b, c = map(int, input().split())
count = 3

if a == b == c:
    print(1)
    return
if a == b:
    count -=1
if a == c:
    count -=1
if b == c:
    count -=1
print(count)
