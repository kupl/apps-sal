n = int(input())
a = list(map(int, input().split()))
s = sum(a)
mx = max(a)
while(n * mx - s <= s):
    mx += 1
print(mx)
