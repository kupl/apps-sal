num, y = map(int, input().split())
inp1 = list(map(int, input().split()))
inp1 = set(inp1)
count1 = 1
s = [0] * 100000
b = 0
while((y - count1) >= 0):
    if(not(count1 in inp1)):
        s[b] = count1
        b += 1
        y -= count1
        inp1.add(count1)
    count1 += 1
print(b)
for j in range(b):
    print(s[j], end=" ")
