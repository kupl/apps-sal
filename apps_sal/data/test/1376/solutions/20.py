n = int(input())
nums = [int(x) for x in input().split()]

coords = {}

for i, k in enumerate(nums):
    if str(k) + "_1" in coords:
        coords[str(k) + "_2"] = i
    else:
        coords[str(k) + "_1"] = i

# print(coords)

s = 0
prev1 = 0
prev2 = 0
for i in range(1, n + 1):
    cur1 = coords[str(i) + "_1"]
    cur2 = coords[str(i) + "_2"]
    #print(prev1, prev2, cur1, cur2)
    d1 = abs(cur1 - prev1) + abs(cur2 - prev2)
    d2 = abs(cur1 - prev2) + abs(cur2 - prev1)
    #print("d1 ", d1, "d2 ", d2)
    s += min(d1, d2)
    prev1 = cur1
    prev2 = cur2
    # print(s)

print(s)
