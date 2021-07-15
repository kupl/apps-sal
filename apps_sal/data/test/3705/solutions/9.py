n = int(input())
s = input()
eight = 0
for x in s:
    if x == '8': eight+=1
print(min(eight, n//11))
