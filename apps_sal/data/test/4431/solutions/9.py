n = input()
s = input()
s += "-"
available = input().split()

length = 0
ans = 0;
for i in s:
    if (i in available):
        length += 1
    else:
        ans += length*(length+1) // 2
        length = 0
        
print(ans)
