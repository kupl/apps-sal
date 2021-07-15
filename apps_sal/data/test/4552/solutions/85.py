def bitcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f #8bitごと
    x = x + (x >> 8) #16bitごと
    x = x + (x >> 16) #32bitごと
    x = x + (x >> 32) #64bitごと = 全部の合計
    return x & 0x0000007f

def binary_to_int(x):
    temp = 0
    for i in range(len(str(x))):
        temp += 2**(len(str(x))-i-1) * int(str(x[i]))
    return temp

n = int(input())
shops = []
for i in range(n):
    shops.append(binary_to_int("".join(input().split())))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, 2**10):
    temp = 0
    for j in range(n):
        temp += p[j-1][bitcount(i & shops[j-1])]
    if i == 1:
        ans = temp
    elif temp > ans:
        ans = temp

print(ans)
