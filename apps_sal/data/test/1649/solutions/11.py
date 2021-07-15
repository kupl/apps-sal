import sys

li = list(map(int, input().split()))
s = sum(li)

if s%2:
    print("No")
    return

for i in range(4):
    for j in range(i+1,4):
        if li[i] + li[j] == s//2 or li[i] == s//2:
            print("Yes")
            return
print("No")
