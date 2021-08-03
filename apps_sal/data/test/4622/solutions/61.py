

n = int(input())
nums = input().split(' ')
nums = [int(x) for x in nums]
s = set()
b = False
for x in nums:
    if x in s:
        print("NO")
        b = True
        break
    s.add(x)
if not b:
    print("YES")
