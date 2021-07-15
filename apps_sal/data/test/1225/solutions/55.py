h = int(input())
count = 0
ans = 0

while h > 0:
    h //= 2
    count += 1

for i in range(count):
    ans = ans*2 + 1

print(ans)
